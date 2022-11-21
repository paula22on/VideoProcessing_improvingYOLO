# This code rotates the ideo frames 90º

import cv2
    
# original video 
cap = cv2.VideoCapture('videos/no_people.m4v')
    
frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Get width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Open the output video file 
newvideoR = cv2.VideoWriter('videos/no_people_r.mp4', cv2.VideoWriter_fourcc(*"mp4v"), 50, (frame_width, frame_height))
    
# Original Frames
for i in range(frame_number):
    ret, frame = cap.read()

    # rotate video
    new = cv2.rotate(frame, cv2.ROTATE_180)
    
    newvideoR.write(new)

newvideoR.release()
cap.release()