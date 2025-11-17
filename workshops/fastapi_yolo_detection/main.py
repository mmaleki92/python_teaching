"""
FastAPI + YOLO Object Detection Workshop
========================================
This application demonstrates how to build a modern REST API using FastAPI
that performs object detection using YOLOv8 model.

Features:
- RESTful API endpoints for object detection
- Async/await patterns for better performance
- Automatic API documentation with Swagger UI
- File upload and image processing
- JSON response with detection results
"""

import os
import uuid
from pathlib import Path
from typing import List, Dict
import shutil

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

# Initialize FastAPI application
app = FastAPI(
    title="YOLO Object Detection API",
    description="REST API for object detection using YOLOv8",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing)
# This allows the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
UPLOAD_FOLDER = "uploads"
RESULTS_FOLDER = "results"
STATIC_FOLDER = "static"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Create necessary folders
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

# Mount static files directory
app.mount("/static", StaticFiles(directory=STATIC_FOLDER), name="static")

# Initialize YOLO model
print("Loading YOLO model...")
model = YOLO('yolov8n.pt')  # Nano version for faster inference
print("Model loaded successfully!")


def allowed_file(filename: str) -> bool:
    """
    Check if the uploaded file has an allowed extension.
    
    Args:
        filename (str): Name of the uploaded file
        
    Returns:
        bool: True if file extension is allowed, False otherwise
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


async def perform_detection(image_path: str, output_path: str) -> List[Dict]:
    """
    Perform object detection on an image using YOLO model.
    
    Args:
        image_path (str): Path to the input image
        output_path (str): Path to save the output image with bounding boxes
        
    Returns:
        List[Dict]: List of dictionaries containing detection results
                   Each dict has: 'class', 'confidence', 'bbox'
    """
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError("Could not read image file")
    
    # Perform detection
    results = model(image)
    
    # Extract detection information
    detections = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Get bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            
            # Get confidence score
            confidence = float(box.conf[0].cpu().numpy())
            
            # Get class name
            class_id = int(box.cls[0].cpu().numpy())
            class_name = model.names[class_id]
            
            # Store detection info
            detections.append({
                'class': class_name,
                'confidence': round(confidence, 4),
                'bbox': {
                    'x1': int(x1),
                    'y1': int(y1),
                    'x2': int(x2),
                    'y2': int(y2)
                }
            })
            
            # Draw bounding box on image
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            
            # Add label with class name and confidence
            label = f"{class_name}: {confidence:.2f}"
            cv2.putText(image, label, (int(x1), int(y1) - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Save the image with bounding boxes
    cv2.imwrite(output_path, image)
    
    return detections


@app.get("/", response_class=HTMLResponse)
async def serve_homepage():
    """
    Serve the main HTML page for the web interface.
    
    Returns:
        HTMLResponse: The HTML content of the homepage
    """
    html_path = Path(STATIC_FOLDER) / "index.html"
    
    if not html_path.exists():
        return HTMLResponse(
            content="<h1>Error: index.html not found in static folder</h1>",
            status_code=404
        )
    
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


@app.post("/api/detect", response_model=None)
async def detect_objects(file: UploadFile = File(...)):
    """
    Upload an image and perform object detection.
    
    Args:
        file (UploadFile): The uploaded image file
        
    Returns:
        JSONResponse: Detection results including:
            - success: boolean indicating success/failure
            - detections: list of detected objects
            - total_objects: number of objects detected
            - image_url: URL to view the processed image
            - original_url: URL to view the original image
            
    Raises:
        HTTPException: If file validation fails or processing error occurs
    """
    # Validate file is provided
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    # Validate file extension
    if not allowed_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Please upload JPG, JPEG, or PNG images."
        )
    
    # Validate file size
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Maximum size is {MAX_FILE_SIZE / 1024 / 1024}MB"
        )
    
    try:
        # Generate unique filename
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}.{file_ext}"
        upload_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        
        # Save uploaded file
        with open(upload_path, "wb") as buffer:
            buffer.write(contents)
        
        # Generate output filename
        output_filename = f"detected_{unique_filename}"
        output_path = os.path.join(RESULTS_FOLDER, output_filename)
        
        # Perform object detection
        detections = await perform_detection(upload_path, output_path)
        
        # Prepare response
        response_data = {
            "success": True,
            "message": "Detection completed successfully",
            "total_objects": len(detections),
            "detections": detections,
            "image_url": f"/images/results/{output_filename}",
            "original_url": f"/images/uploads/{unique_filename}",
            "filename": file.filename
        }
        
        return JSONResponse(content=response_data)
        
    except Exception as e:
        # Clean up files if they exist
        if os.path.exists(upload_path):
            os.remove(upload_path)
        if os.path.exists(output_path):
            os.remove(output_path)
            
        raise HTTPException(
            status_code=500,
            detail=f"Error processing image: {str(e)}"
        )


@app.get("/images/uploads/{filename}")
async def get_uploaded_image(filename: str):
    """
    Retrieve an uploaded image.
    
    Args:
        filename (str): Name of the uploaded file
        
    Returns:
        FileResponse: The requested image file
        
    Raises:
        HTTPException: If file not found
    """
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found")
    
    return FileResponse(file_path)


@app.get("/images/results/{filename}")
async def get_result_image(filename: str):
    """
    Retrieve a processed result image.
    
    Args:
        filename (str): Name of the result file
        
    Returns:
        FileResponse: The requested image file
        
    Raises:
        HTTPException: If file not found
    """
    file_path = os.path.join(RESULTS_FOLDER, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found")
    
    return FileResponse(file_path)


@app.get("/api/health")
async def health_check():
    """
    Health check endpoint to verify API is running.
    
    Returns:
        Dict: Status information
    """
    return {
        "status": "healthy",
        "model": "YOLOv8n",
        "version": "1.0.0"
    }


@app.get("/api/supported-objects")
async def get_supported_objects():
    """
    Get list of object classes that can be detected.
    
    Returns:
        Dict: List of supported object classes
    """
    return {
        "total_classes": len(model.names),
        "classes": list(model.names.values())
    }


@app.delete("/api/cleanup")
async def cleanup_files():
    """
    Clean up uploaded and result files (for development/testing).
    
    Returns:
        Dict: Cleanup status
    """
    try:
        # Remove all files in upload folder
        for file in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        # Remove all files in results folder
        for file in os.listdir(RESULTS_FOLDER):
            file_path = os.path.join(RESULTS_FOLDER, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        return {
            "success": True,
            "message": "All temporary files cleaned up"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error cleaning up files: {str(e)}"
        )


# Entry point for running the application
if __name__ == "__main__":
    import uvicorn
    
    # Run the FastAPI application
    # Access the API at: http://localhost:8000
    # Access API docs at: http://localhost:8000/docs
    # Access ReDoc at: http://localhost:8000/redoc
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Enable auto-reload during development
    )
