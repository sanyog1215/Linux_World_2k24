import cv2

def capture_and_process_image():
    # Initialize the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    
    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Capture the image from the webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture image")
        return

    # Convert the image to grayscale (needed for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("No face detected")
        return
    
    # Process each face found
    for (x, y, w, h) in faces:
        # Crop the face from the original image
        face = frame[y:y+h, x:x+w]
        
        # Resize the face to a smaller size (optional, for better overlay)
        face_resized = cv2.resize(face, (w//2, h//2))
        
        # Overlay the cropped face back onto the main image at the top-left corner
        frame[0:face_resized.shape[0], 0:face_resized.shape[1]] = face_resized
        
        # Draw a rectangle around the detected face in the main image
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the result
    cv2.imshow('Image with Cropped Face', frame)
    
    # Wait for a key press and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Release the camera
    cap.release()

# Run the function
capture_and_process_image()
