# Invisible Cloak

This project implements an "Invisible Cloak" effect using Python and OpenCV.
It captures a background image, detects a specific colored cloak (default is red) in the real-time webcam feed, and replaces the cloak's area with the background, creating the illusion of invisibility.

## Requirements
- Python 3
- OpenCV
- NumPy
- Webcam

## Installation
1. Ensure you have Python installed.
2. Install the required dependencies:
```bash
pip install opencv-python numpy
```

## How to Run
1. Run the script:
```bash
python invisible_cloak.py
```
2. Make sure the webcam has a clear view of the background. Let it capture the background for the first few seconds without moving any objects or entering the frame.
3. Once the background is captured (you will see a console message indicating this), step into the frame with your red cloak.
4. Press `q` to quit the application.

## Reference
See `Invisible_Cloak_OpenCV_Project_Report.pdf` for more details on the system architecture, DFD, and steps used in this project.