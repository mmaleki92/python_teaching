# Flask + YOLO Object Detection Workshop

This workshop demonstrates how to build a web application using Flask that performs real-time object detection using YOLOv8 (You Only Look Once) deep learning model.

## 📋 Project Description

This application allows users to:
- Upload images through a user-friendly web interface
- Perform object detection using the state-of-the-art YOLOv8 model
- View results with bounding boxes drawn around detected objects
- See a list of all detected objects with their confidence scores
- Download the processed images

## 🎯 Learning Objectives

By completing this workshop, you will learn:
- How to build a Flask web application
- How to handle file uploads in Flask
- How to integrate machine learning models (YOLO) into web applications
- How to process images using OpenCV and YOLO
- How to create responsive HTML templates with Jinja2
- How to serve static files and dynamic content
- Error handling and input validation in web applications

## 🛠️ Technologies Used

- **Flask**: Web framework for Python
- **YOLOv8**: State-of-the-art object detection model
- **OpenCV**: Computer vision library for image processing
- **Pillow**: Python Imaging Library
- **HTML/CSS/JavaScript**: Frontend technologies

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone the repository** (if not already done):
   ```bash
   cd workshops/flask_yolo_detection
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
   - Flask (web framework)
   - ultralytics (YOLO model)
   - opencv-python (image processing)
   - Pillow (image handling)
   - numpy (numerical operations)

5. **First run - YOLO model download**:
   
   On the first run, YOLOv8 will automatically download the pre-trained model (~6MB for nano version). This happens automatically when you start the application.

## 🚀 How to Run

1. **Activate your virtual environment** (if not already activated)

2. **Run the Flask application**:
   ```bash
   python app.py
   ```

3. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

4. **You should see**:
   - A beautiful, modern web interface
   - A file upload area
   - Instructions on how to use the application

## 📖 Usage Guide

### Uploading an Image

1. Click on the upload area or drag and drop an image
2. Select an image file (JPG, JPEG, or PNG format)
3. Click "Detect Objects" button
4. Wait for processing (usually takes 1-3 seconds)

### Viewing Results

The results page displays:
- **Original Image**: Your uploaded image
- **Detected Objects Image**: Image with bounding boxes and labels
- **Detection Statistics**:
  - Number of objects detected
  - Average confidence score
  - Number of unique object classes
- **Detailed List**: Each detected object with:
  - Object class/name
  - Confidence score (0-100%)
  - Visual confidence bar

### Supported Objects

YOLOv8 can detect 80 different object classes, including:
- People, animals (cat, dog, bird, horse, etc.)
- Vehicles (car, truck, bus, motorcycle, bicycle, etc.)
- Indoor objects (chair, table, sofa, bed, etc.)
- Electronics (TV, laptop, keyboard, mouse, etc.)
- Kitchen items (bottle, cup, fork, knife, etc.)
- And many more!

## 🎨 Example Usage

### Example 1: Detecting Objects in a Street Photo

1. Upload a photo of a street scene
2. The model will detect: cars, people, traffic lights, bicycles, etc.
3. Each object will be highlighted with a green bounding box
4. Confidence scores typically range from 70-95% for clear objects

### Example 2: Detecting Objects in a Room

1. Upload a photo of a room
2. The model will detect: furniture, electronics, decorations, etc.
3. Multiple instances of the same object will all be detected
4. Lower confidence scores (50-70%) might appear for partially visible objects

## 📁 Project Structure

```
flask_yolo_detection/
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html        # Homepage with upload form
│   └── results.html      # Results display page
├── uploads/              # Uploaded images (created automatically)
├── results/              # Processed images (created automatically)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔧 Configuration

You can modify the following settings in `app.py`:

- **YOLO Model**: Change `yolov8n.pt` to:
  - `yolov8s.pt` - Small (faster, less accurate)
  - `yolov8m.pt` - Medium (balanced)
  - `yolov8l.pt` - Large (slower, more accurate)
  - `yolov8x.pt` - Extra large (slowest, most accurate)

- **Max File Size**: Modify `MAX_CONTENT_LENGTH` (default: 16MB)

- **Allowed Extensions**: Modify `ALLOWED_EXTENSIONS` set

- **Server Port**: Change `port=5000` in the last line

## 🐛 Troubleshooting

### Common Issues

1. **Module not found errors**:
   - Make sure you activated the virtual environment
   - Run `pip install -r requirements.txt` again

2. **YOLO model not downloading**:
   - Check your internet connection
   - The model downloads automatically on first run
   - Manual download: The model is stored in `~/.cache/torch/hub/`

3. **Image upload fails**:
   - Check file size (must be under 16MB)
   - Ensure file format is JPG, JPEG, or PNG
   - Check file permissions

4. **Port already in use**:
   - Change the port number in `app.py`
   - Or stop other applications using port 5000

### Error Messages

- **"No file uploaded"**: Make sure to select a file before clicking submit
- **"Invalid file type"**: Only JPG, JPEG, and PNG files are supported
- **"Error processing image"**: The image might be corrupted or in an unsupported format

## 🎓 Learning Resources

### Understanding the Code

**Flask Routes**:
- `/` - Homepage with upload form
- `/upload` - Handles file upload and processing (POST)
- `/results` - Displays detection results
- `/uploads/<filename>` - Serves uploaded images
- `/results/<filename>` - Serves processed images

**Key Functions**:
- `allowed_file()` - Validates file extensions
- `perform_detection()` - Runs YOLO model and draws bounding boxes
- `upload_file()` - Handles the upload process
- `results()` - Displays detection results

### YOLOv8 Basics

YOLO (You Only Look Once) is a state-of-the-art object detection model that:
- Processes images in real-time
- Detects multiple objects simultaneously
- Provides bounding box coordinates and confidence scores
- Can identify 80 different object classes

### Next Steps

To enhance this project, you could:
1. Add video processing capability
2. Implement real-time webcam detection
3. Add a database to store detection history
4. Create user accounts and authentication
5. Deploy to a cloud platform (Heroku, AWS, etc.)
6. Add custom object detection for specific use cases
7. Implement object tracking across video frames

## 📝 Notes for Instructors

This workshop is designed to be:
- **Beginner-friendly**: Clear comments and explanations
- **Self-contained**: All files included, no external dependencies
- **Interactive**: Visual feedback and real-time results
- **Educational**: Demonstrates best practices in web development

**Recommended Teaching Order**:
1. Explain Flask basics and routing
2. Demonstrate file upload handling
3. Introduce YOLO and object detection concepts
4. Walk through the image processing pipeline
5. Show template rendering with Jinja2
6. Discuss error handling and validation

**Time Estimate**: 2-3 hours for complete workshop

## 🤝 Contributing

This is a teaching project. Feel free to:
- Add new features
- Improve the UI/UX
- Fix bugs
- Enhance documentation
- Add more examples

## 📄 License

This project is created for educational purposes as part of Python teaching materials.

## 🌟 Acknowledgments

- **Ultralytics** for the YOLOv8 implementation
- **Flask** team for the excellent web framework
- **OpenCV** community for computer vision tools

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Review the code comments
3. Consult Flask and YOLO documentation
4. Ask your instructor or classmates

---

**Happy Learning! 🎉**

Remember: The best way to learn is by doing. Try modifying the code, experimenting with different settings, and building upon this foundation!
