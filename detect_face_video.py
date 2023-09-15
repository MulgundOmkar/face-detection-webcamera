#computer vision(cv2) library should be installed
import cv2

# Load the cascade(pre-trained dectetor) only it can detect the front face 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from laptopcamera(webcam)  
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    
    _, img = cap.read()

    # Convert to grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    #four parameters x,y,w,h are the cordinates
    for (x, y, w, h) in faces:
        #can change the color of the rectangle by changing the parameters
        #Default color is green 
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display of video
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    #press any key to exit While True will always be true so to exit from the loop 
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the videocapture object exit
cap.release()