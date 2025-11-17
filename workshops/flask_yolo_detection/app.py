"""
Flask + YOLO Object Detection Workshop
======================================
This application demonstrates how to build a web application using Flask
that performs object detection using YOLOv8 model.

Features:
- Upload images through a web interface
- Perform object detection using YOLOv8
- Display results with bounding boxes
- Show detected objects with confidence scores
"""

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import cv2
from pathlib import Path

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'results'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Create necessary folders if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)

# Initialize YOLO model (YOLOv8n - nano version for faster inference)
# The model will be downloaded automatically on first use
print("Loading YOLO model...")
model = YOLO('yolov8n.pt')  # You can use yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt for better accuracy
print("Model loaded successfully!")


def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    
    Args:
        filename (str): Name of the uploaded file
        
    Returns:
        bool: True if file extension is allowed, False otherwise
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def perform_detection(image_path, output_path):
    """
    Perform object detection on an image using YOLO model.
    
    Args:
        image_path (str): Path to the input image
        output_path (str): Path to save the output image with bounding boxes
        
    Returns:
        list: List of dictionaries containing detection results
              Each dict has: 'class', 'confidence', 'bbox'
    """
    # Read the image
    image = cv2.imread(image_path)
    
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
                'confidence': confidence,
                'bbox': [int(x1), int(y1), int(x2), int(y2)]
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


@app.route('/')
def index():
    """
    Render the homepage with file upload form.
    """
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload and perform object detection.
    
    Returns:
        Redirect to results page or error page
    """
    # Check if file was uploaded
    if 'file' not in request.files:
        return render_template('index.html', error='No file uploaded')
    
    file = request.files['file']
    
    # Check if filename is empty
    if file.filename == '':
        return render_template('index.html', error='No file selected')
    
    # Check if file type is allowed
    if not allowed_file(file.filename):
        return render_template('index.html', 
                             error='Invalid file type. Please upload JPG, JPEG, or PNG images.')
    
    try:
        # Save the uploaded file
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        
        # Generate output filename
        output_filename = f"detected_{filename}"
        output_path = os.path.join(app.config['RESULTS_FOLDER'], output_filename)
        
        # Perform object detection
        detections = perform_detection(upload_path, output_path)
        
        # Redirect to results page
        return redirect(url_for('results', 
                              original=filename, 
                              detected=output_filename))
    
    except Exception as e:
        return render_template('index.html', 
                             error=f'Error processing image: {str(e)}')


@app.route('/results')
def results():
    """
    Display detection results with images and detected objects.
    """
    original_filename = request.args.get('original')
    detected_filename = request.args.get('detected')
    
    if not original_filename or not detected_filename:
        return redirect(url_for('index'))
    
    # Load detection results
    output_path = os.path.join(app.config['RESULTS_FOLDER'], detected_filename)
    
    # Re-run detection to get detection info (in production, you'd store this)
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
    detections = perform_detection(upload_path, output_path)
    
    return render_template('results.html',
                         original_image=original_filename,
                         detected_image=detected_filename,
                         detections=detections)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    Serve uploaded files.
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/results/<filename>')
def result_file(filename):
    """
    Serve result files with bounding boxes.
    """
    return send_from_directory(app.config['RESULTS_FOLDER'], filename)


if __name__ == '__main__':
    # Run the Flask application
    # Debug mode is enabled for development/workshop purposes only
    # WARNING: Never use debug=True in production environments!
    # For production, use a production WSGI server like Gunicorn or uWSGI
    # Example: gunicorn -w 4 -b 0.0.0.0:5000 app:app
    
    # Use environment variable to control debug mode (defaults to True for workshop)
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
