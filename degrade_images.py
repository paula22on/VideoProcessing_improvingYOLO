# This python file aims to degrade the quality of the image by downsampling it
import os
import cv2
import glob


# Function for donwsampling the video frames
def degrade_images(path, factor):

    # loop through the files in the directory
    for file in os.listdir(path):
        # open the file
        img = cv2.imread(path + '/' + file)
        
        # find old and new image dimensions
        h, w, _ = img.shape
        new_height = int(h / factor)
        new_width = int(w / factor)
        
        # resize the image - down
        img = cv2.resize(img, (new_width, new_height), interpolation = cv2.INTER_LINEAR)
        
        # resize the image - up
        # img = cv2.resize(img, (w, h), interpolation = cv2.INTER_LINEAR)

        # save the image
        print('Saving {}'.format(file))
        cv2.imwrite('degraded_video_frames/{}'.format(file), img)

path = 'ImageSuperResolution/video_frames'
factor = 2
# degrade_images(path, factor) #downsample video frames


# Get filename to have the frames ordered before converting to video
name = '/content/Super_resolution_videos/'

# Get ordered frames for converting to video
filenames = []
for i in range(114):
  filenames.append('degraded_video_frames/Frame' + str(i) + '.jpg')

# Convert frames to video
img_array = []
for filename in filenames:
  img = cv2.imread(filename)
  height, width, layers = img.shape
  size = (width, height)
  img_array.append(img)

out = cv2.VideoWriter('degraded_video.mp4v', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
  out.write(img_array[i])
out.release()
    




        
 