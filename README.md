Real-Time Face Detection
Overview
This project is a Python application that uses OpenCV and a Haar Cascade classifier to detect faces in real-time using your webcam.
Features
Real-time Monitoring: Live video feed from the default camera.
Visual Indicators: Draws green bounding boxes around detected faces.
Face Counter: Displays the number of faces detected on-screen.
Controls: Press 's' to take a screenshot, Press 'q' to quit.
Technologies Used
Python 3.x
OpenCV (cv2)
Haar Cascade Classifier (Pre-trained model)
Installation & Execution
Install OpenCV:
Bash
pip install opencv-python
Run the Script:
Bash
python face_detection.py
Testing Instructions
Run the script; the webcam window will open.
Position yourself in the frame; verify a green rectangle appears around your face.
Press 's' to save a screenshot (check the project folder for screenshot_x.jpg).
Press 'q' to close the program.
