# This file contains code to trasnform RGB images to HSV and HSL
import numpy as np
import cv2

# Capture video from camera
# cap = cv2.VideoCapture(0)

# Capture video from file
cap = cv2.VideoCapture('videos/1.mp4')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('videos/1_hsl.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (frame_width,frame_height))

HSV = True
HSL = True

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if HSV:
        # Our operations on the frame come here
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Modify hue
        hsv[...,0] = hsv[...,0]*0.9

        # Multiple by a factor to change the saturation
        hsv[...,1] = hsv[...,1]*1.35

        # Multiple by a factor of less than 1 to reduce the brightness 
        hsv[...,2] = hsv[...,2]*1

        hsv=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

        out.write(hsv)

        # Display the resulting frame
        cv2.imshow('frame',hsv)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    if HSL:

        # Our operations on the frame come here
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        hsl = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
        
        #modify hue
        # hsl[...,0] = hsl[...,0]*1

        #multiple by a factor to change the saturation
        hsl[...,1] = hsl[...,1]*0.5

        #multiple by a factor of less than 1 to reduce the brightness 
        hsl[...,2] = hsl[...,2]*0.5

        hsl=cv2.cvtColor(hsl,cv2.COLOR_HLS2RGB)
        hsl=cv2.cvtColor(hsl,cv2.COLOR_RGB2BGR)

        out.write(hsl)

        # Display the resulting frame
        cv2.imshow('frame',hsl)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()