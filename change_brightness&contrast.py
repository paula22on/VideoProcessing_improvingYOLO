# This code is for modifying the brightness and contrast of a given image
import numpy as np
import cv2

# Capture video from file
cap = cv2.VideoCapture('videos/riyadh_video.mp4v')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('videos/riyadh_video_contrastbrighntess.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 25, (frame_width,frame_height))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #change colorspace 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #modify contrast and brightness
    contrast = 0.5
    brightness = 2
    frame[:,:,2] = np.clip(contrast * frame[:,:,2] + brightness, 0, 255)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame',frame)
  
    
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()