# FastAPI + YOLO Object Detection Workshop

This workshop demonstrates how to build a modern REST API using FastAPI that performs real-time object detection using YOLOv8 (You Only Look Once) deep learning model.

## 📋 Project Description

This application provides a RESTful API for object detection with:
- Modern async/await patterns for better performance
- Automatic interactive API documentation (Swagger UI)
- Clean JSON responses with detection results
- File upload and image processing capabilities
- Frontend interface for easy testing
- Multiple API endpoints for various operations

## 🎯 Learning Objectives

By completing this workshop, you will learn:
- How to build a FastAPI application with async/await
- RESTful API design principles
- How to handle file uploads in FastAPI
- How to integrate YOLO object detection models
- Image processing with OpenCV
- API documentation with Swagger/OpenAPI
- CORS (Cross-Origin Resource Sharing) configuration
- Error handling and HTTP exceptions
- Frontend-backend communication with async JavaScript

## 🛠️ Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running the application
- **YOLOv8**: State-of-the-art object detection model
- **OpenCV**: Computer vision library
- **Python-multipart**: For handling file uploads
- **HTML/CSS/JavaScript**: Frontend interface

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Navigate to the project directory**:
   ```bash
   cd workshops/fastapi_yolo_detection
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - fastapi (modern web framework)
   - uvicorn (ASGI server)
   - python-multipart (file upload support)
   - ultralytics (YOLO implementation)
   - opencv-python (image processing)
   - Pillow (image handling)
   - numpy (numerical operations)

5. **First run - YOLO model download**:
   
   On the first run, YOLOv8 will automatically download the pre-trained model (~6MB for nano version).

## 🚀 How to Run

### Option 1: Using Python directly

```bash
python main.py
```

### Option 2: Using Uvicorn command

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The `--reload` flag enables auto-reload during development.

### Accessing the Application

Once running, you can access:

1. **Web Interface**: http://localhost:8000
   - User-friendly interface for uploading and detecting objects

2. **Interactive API Docs (Swagger UI)**: http://localhost:8000/docs
   - Try out API endpoints directly from the browser
   - See request/response schemas
   - Test authentication and file uploads

3. **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc
   - Clean, readable documentation
   - Better for sharing with team members

## 📖 API Endpoints Documentation

### 1. Homepage
- **Endpoint**: `GET /`
- **Description**: Serves the web interface
- **Response**: HTML page

### 2. Detect Objects
- **Endpoint**: `POST /api/detect`
- **Description**: Upload an image and perform object detection
- **Parameters**: 
  - `file` (form-data): Image file (JPG, JPEG, or PNG)
- **Response**:
  ```json
  {
    "success": true,
    "message": "Detection completed successfully",
    "total_objects": 5,
    "detections": [
      {
        "class": "person",
        "confidence": 0.9234,
        "bbox": {
          "x1": 100,
          "y1": 150,
          "x2": 300,
          "y2": 450
        }
      }
    ],
    "image_url": "/images/results/detected_abc123.jpg",
    "original_url": "/images/uploads/abc123.jpg",
    "filename": "my_photo.jpg"
  }
  ```

### 3. Health Check
- **Endpoint**: `GET /api/health`
- **Description**: Check if API is running
- **Response**:
  ```json
  {
    "status": "healthy",
    "model": "YOLOv8n",
    "version": "1.0.0"
  }
  ```

### 4. Supported Objects
- **Endpoint**: `GET /api/supported-objects`
- **Description**: Get list of detectable object classes
- **Response**:
  ```json
  {
    "total_classes": 80,
    "classes": ["person", "bicycle", "car", ...]
  }
  ```

### 5. Get Image
- **Endpoint**: `GET /images/uploads/{filename}`
- **Description**: Retrieve uploaded image
- **Response**: Image file

### 6. Get Result Image
- **Endpoint**: `GET /images/results/{filename}`
- **Description**: Retrieve processed image with bounding boxes
- **Response**: Image file

### 7. Cleanup (Development Only)
- **Endpoint**: `DELETE /api/cleanup`
- **Description**: Remove all temporary files
- **Response**:
  ```json
  {
    "success": true,
    "message": "All temporary files cleaned up"
  }
  ```

## 💻 Usage Examples

### Using cURL

**Upload and detect objects**:
```bash
curl -X POST "http://localhost:8000/api/detect" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/your/image.jpg"
```

**Health check**:
```bash
curl http://localhost:8000/api/health
```

**Get supported objects**:
```bash
curl http://localhost:8000/api/supported-objects
```

### Using Python Requests

```python
import requests

# Upload and detect
with open('image.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/api/detect', files=files)
    result = response.json()
    print(f"Detected {result['total_objects']} objects")
    for detection in result['detections']:
        print(f"- {detection['class']}: {detection['confidence']:.2%}")

# Health check
response = requests.get('http://localhost:8000/api/health')
print(response.json())
```

### Using JavaScript (Frontend)

```javascript
// Upload and detect
const formData = new FormData();
formData.append('file', fileInput.files[0]);

const response = await fetch('/api/detect', {
    method: 'POST',
    body: formData
});

const data = await response.json();
console.log(`Detected ${data.total_objects} objects`);
```

## 📁 Project Structure

```
fastapi_yolo_detection/
├── main.py                # Main FastAPI application
├── static/
│   ├── index.html        # Frontend interface
│   └── style.css         # Styling
├── uploads/              # Uploaded images (created automatically)
├── results/              # Processed images (created automatically)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔧 Configuration Options

You can modify these settings in `main.py`:

### YOLO Model Selection
```python
# Choose model based on your needs:
model = YOLO('yolov8n.pt')  # Nano - fastest, least accurate
model = YOLO('yolov8s.pt')  # Small
model = YOLO('yolov8m.pt')  # Medium - balanced
model = YOLO('yolov8l.pt')  # Large
model = YOLO('yolov8x.pt')  # Extra Large - slowest, most accurate
```

### Server Configuration
```python
# In main.py, at the bottom:
uvicorn.run(
    "main:app",
    host="0.0.0.0",      # Listen on all interfaces
    port=8000,            # Change port if needed
    reload=True           # Auto-reload on code changes (development only)
)
```

### File Upload Limits
```python
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
```

## 🐛 Troubleshooting

### Common Issues

1. **Module not found errors**:
   ```bash
   # Ensure virtual environment is activated
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. **Port already in use**:
   ```bash
   # Change port in main.py or use a different port:
   uvicorn main:app --port 8001
   ```

3. **YOLO model download fails**:
   - Check internet connection
   - Model downloads automatically to `~/.cache/torch/hub/`
   - Retry - it will resume interrupted downloads

4. **CORS errors in browser**:
   - Already configured for development (`allow_origins=["*"]`)
   - For production, specify exact origins in `CORSMiddleware`

5. **File upload fails**:
   - Check file size (max 16MB)
   - Verify file format (JPG, JPEG, PNG only)
   - Check server logs for detailed error messages

### Debug Mode

Enable detailed logging:
```bash
uvicorn main:app --reload --log-level debug
```

## 🎓 Learning Resources

### FastAPI Concepts Demonstrated

1. **Async/Await**: Efficient handling of I/O operations
2. **Dependency Injection**: Clean, testable code structure
3. **Request Validation**: Automatic with Pydantic
4. **Exception Handling**: HTTP exceptions with proper status codes
5. **File Uploads**: Handling multipart form data
6. **Static Files**: Serving frontend assets
7. **Auto Documentation**: OpenAPI/Swagger integration

### API Design Best Practices

- **RESTful Endpoints**: Clear, predictable URL structure
- **HTTP Methods**: Proper use of GET, POST, DELETE
- **Status Codes**: Appropriate responses (200, 400, 404, 500)
- **JSON Responses**: Consistent response format
- **Error Messages**: Helpful, actionable error descriptions

### Next Steps

Enhance this project by:
1. **Add Authentication**: JWT tokens, OAuth2
2. **Database Integration**: Store detection history with SQLAlchemy
3. **Batch Processing**: Handle multiple images at once
4. **Video Support**: Process video files frame by frame
5. **WebSocket**: Real-time detection updates
6. **Model Selection**: Let users choose YOLO model version
7. **Custom Training**: Fine-tune YOLO for specific objects
8. **Docker**: Containerize the application
9. **Cloud Deployment**: Deploy to AWS, GCP, or Azure
10. **Testing**: Add unit and integration tests with pytest

## 📊 Performance Considerations

### Model Performance
- **YOLOv8n**: ~5-10ms per image (CPU), ~1-2ms (GPU)
- **YOLOv8s**: ~10-15ms per image (CPU), ~2-3ms (GPU)
- **YOLOv8m**: ~15-25ms per image (CPU), ~3-5ms (GPU)

### Optimization Tips
1. Use smaller model (nano/small) for faster inference
2. Resize large images before processing
3. Implement caching for repeated detections
4. Use GPU if available (CUDA-enabled PyTorch)
5. Batch process multiple images together

## 🔒 Security Considerations

For production deployment:
1. **File Validation**: Verify file content, not just extension
2. **Rate Limiting**: Prevent API abuse
3. **CORS**: Restrict to specific origins
4. **File Size Limits**: Already implemented (16MB)
5. **Sanitize Filenames**: Already using UUID for safety
6. **HTTPS**: Use TLS/SSL in production
7. **Authentication**: Add API keys or OAuth2
8. **Input Validation**: Already implemented with FastAPI

## 📝 Notes for Instructors

This workshop is designed to:
- Demonstrate modern API development with FastAPI
- Show async programming patterns in Python
- Integrate machine learning models into web applications
- Teach REST API best practices
- Provide hands-on experience with real-world tools

**Recommended Teaching Order**:
1. Explain FastAPI basics and advantages over Flask
2. Demonstrate async/await patterns
3. Show automatic documentation features
4. Walk through file upload handling
5. Introduce YOLO and object detection
6. Test API with Swagger UI
7. Demonstrate frontend-backend communication
8. Discuss deployment considerations

**Time Estimate**: 2-3 hours for complete workshop

**Prerequisites**: 
- Basic Python knowledge
- Understanding of HTTP/REST concepts
- Familiarity with async programming (helpful but not required)

## 🤝 Contributing

This is a teaching project. Contributions welcome:
- Bug fixes
- Documentation improvements
- New features
- Performance optimizations
- Additional examples

## 📄 License

This project is created for educational purposes as part of Python teaching materials.

## 🌟 Acknowledgments

- **FastAPI** team for the excellent framework
- **Ultralytics** for YOLOv8 implementation
- **Starlette** for ASGI foundation
- **Pydantic** for data validation
- **OpenCV** community for computer vision tools

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Review API documentation at `/docs`
3. Check FastAPI documentation
4. Review code comments
5. Ask your instructor

---

**Happy Coding! 🚀**

FastAPI makes building APIs fast and fun. Experiment with the code, try new features, and build something amazing!
