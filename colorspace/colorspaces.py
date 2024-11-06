import cv2 as cv
import os

# path
path = os.path.join(".", "cat1.png")

# read
img = cv.imread(path)

# convert the colorspace of a pixel (bgr to rgb - switing the the colors)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# frame
cv.imshow("img", img) #bgr (3 channel)
cv.imshow("rgb_img", rgb_img) #rgb (3 channel)
cv.imshow("gray_img", gray_img) #gray scale (3 chanel to one channel - less info)
cv.waitKey(0)

# note: (BGR color spaces)
# 1. every time we read an image using imread(), the image will be in the BGR color space - all the pixels are a 
# combination of BGR colors.

# 2. any image read by opencv will be in BGR color space!

# 3. differnt way to express the info of a image - same information but how they are organized is different 

# 4. bgr to grayscale means condensing 3 chnl to only 1 (reduced info and so less storage and easy to work!)

# HSV
# has very imp application - eg: trying to detect color

# different colorspace has different usecase - for human eyes it may be usless but for computers its not. 
