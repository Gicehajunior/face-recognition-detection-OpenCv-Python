import cv2
import sys
import playsound

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# capture video using cv2
video_capture = cv2.VideoCapture(0)

while True:
    # capture frame by frame, i.e, one by one 
    ret, frame = video_capture.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # for each face on the projected on the frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5, 
        # minSize(35, 35)
    )
    
    # loop through the video faces for detection
    for (x, y, w, h) in faces:
        point1 = x+w
        point2 = y+h
        frame_color = (50, 50, 200)
        
        rectangleBox = cv2.rectangle(frame, (x, y), (point1, point2), frame_color, 2)
        cv2.imshow('video', frame)
        if faces.any():
            playsound.playsound('openDoorAlert.mp3', True)
            
            if len(faces) > 1:
                print("There are " + str(len(faces)) + " peoples at the gate")
            else:
                print("There is " + str(len(faces)) + " person at the gate")
        else:
            pass
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sys.exit()
        
