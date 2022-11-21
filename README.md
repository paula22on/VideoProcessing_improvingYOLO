# Video and Image Processing techniques to improve YOLO performance 

This folder contains a set of files with different Image and Video Processing techniques.

## Estructure of the folder:
- Codes applying Image and Video Processing techniques
  - change_brightness&contrast.py
  - change_colors.ipynb
  - change_colorspace.py
  - degrade_images.py
  - invert_color.py
  - normalize.py
  - rotate_video.py
- ImageSuperResolution: folder with all the codes for applying Image Super Resolution
- videos: folder with different videos for the the testing as well as see the results
- images: folder with different images for the the testing as well as see the results 

## Codes:
#### change_brightness&contrast.py
This code is used to change the brightness and contrast of an image transforming the image from BGR to HSV.

#### change_colors.ipynb
In this notebook there are different tests for changing the colors of the images. 
  Test1: removing blue values from an image
  Test2: get more vibrant colors (using HSV)
  Test3: transform image to grayscale
  
#### change_colorspace.py
This code has the implementation for transforming BGR images to HSV and HSL. With this transformations it is also posible to modify the hue, saturation, value and luminance values and change the aspect of the image.

#### degrade_images.py
This code contains the implementation of a function for degrading the frames quality and then megre them again together to obtain the low quality video.

#### invert_color.py
This file contains two functions that invert the color of the images .

#### normalize.py
This file reads a video and performs a normalization for each frame.

#### rotate_video.py
This file contatins the implementation for rotating a video 180º
