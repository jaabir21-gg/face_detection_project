import cv2
import sys

def main():
    """
    Real-time Face Detection using OpenCV
    This program captures video from your webcam and detects faces in real-time.
    """
    
    # Load the pre-trained Haar Cascade classifier for face detection
    # This is a machine learning model that OpenCV provides
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Initialize webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not access the camera")
        sys.exit()
    
    print("Camera opened successfully!")
    print("Press 'q' to quit")
    print("Press 's' to save a screenshot")
    
    screenshot_count = 0
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture frame")
            break
        
        # Convert frame to grayscale (face detection works better on grayscale)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        # Parameters explanation:
        # - scaleFactor: how much the image size is reduced at each scale
        # - minNeighbors: how many neighbors each rectangle should have to be considered a face
        # - minSize: minimum possible face size
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            # Draw a green rectangle around each face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Add a label above each face
            cv2.putText(frame, 'Face', (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Display the number of faces detected
        face_count_text = f'Faces Detected: {len(faces)}'
        cv2.putText(frame, face_count_text, (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Display the resulting frame
        cv2.imshow('Face Detection - Press Q to quit', frame)
        
        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        
        # Press 'q' to quit
        if key == ord('q'):
            print("Quitting...")
            break
        
        # Press 's' to save screenshot
        elif key == ord('s'):
            screenshot_count += 1
            filename = f'screenshot_{screenshot_count}.jpg'
            cv2.imwrite(filename, frame)
            print(f"Screenshot saved as {filename}")
    
    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
    print("Program ended successfully")

if __name__ == "__main__":
    main()