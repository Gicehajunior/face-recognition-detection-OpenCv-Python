import cv2
import sys
from pydub import AudioSegment
from pydub.playback import play


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
        showFrame = ""
        alert
        
        cv2.rectangle(frame, (x, y), (point1, point2), frame_color, 2)
        showFrame = cv2.imshow('video', frame)
        if showFrame:
            alert = AudioSegment.from_mp3('openDoorAlert.mp3')
            play(alert)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sys.exit()
        
