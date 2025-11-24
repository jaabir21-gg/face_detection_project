Real-Time Face Detection System
Overview
This project is a Python-based computer vision application that performs real-time face detection using a webcam. It utilizes the OpenCV library and pre-trained Haar Cascade classifiers to identify human faces within a video stream. The program draws bounding boxes around detected faces, provides a live count of faces in the frame, and allows users to capture screenshots during operation.

Features
Real-time Detection: Captures video feed instantly from the default webcam (Input 0).

Face Highlighting: Draws a green rectangle around detected faces for visual verification.

Live Counter: Displays a real-time count of the total number of faces detected in the current frame.

Screenshot Capability: Allows the user to save the current frame as an image file (.jpg) by pressing a hotkey.

Robust Configuration: Uses specific parameters (Scale Factor 1.1, Min Neighbors 5) to balance detection accuracy and noise reduction.

Grayscale Processing: Converts frames to grayscale internally to improve detection efficiency while displaying the result in color.

Technologies & Tools Used
Programming Language: Python 3.x

Computer Vision Library: OpenCV (opencv-python)


Steps to Install & Run
1. Prerequisites
Ensure you have Python installed on your system. You can verify this by running:

Bash

python --version
2. Install Dependencies
This project requires the OpenCV library. Install it using pip:

Bash

pip install opencv-python
3. Save the Script
Save the provided code into a file named face_detection.py.

4. Run the Project
Open your terminal or command prompt, navigate to the directory containing the file, and run:

Bash

python face_detection.py
Instructions for Testing
Start the Application: Run the command mentioned above. The webcam light should turn on, and a window titled "Face Detection - Press Q to quit" will appear.

Verify Detection: Position yourself in front of the camera. You should see a green rectangle appear around your face and the label "Face" above it.

Check the Counter: Look at the top-left corner of the video window. It should read Faces Detected: 1 (or more if multiple people are in the frame).

Test Screenshots:

Press the 's' key on your keyboard.

Check your project folder/directory. You should see a file named screenshot_1.jpg created.

The console will output: Screenshot saved as screenshot_1.jpg.

Quit: Press the 'q' key to close the window and release the camera safely.
