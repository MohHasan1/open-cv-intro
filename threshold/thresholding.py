# simple/standard threshold
import cv2 as cv
import os

# path
path = os.path.join(".", "cat1.png")

# read
img = cv.imread(path)

# convert to gayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# threshold - simple (global) threshhld (80 for eg) - arg -> (gray scale img, threshold, maxvale, threshold type)
ret, th_img = cv.threshold(gray_img, 80, 255, cv.THRESH_BINARY)
# pixels under 80 will be taken to 0 
# pixels above 80 will be taken to 255

# remove noise - blur (more clear)
blur_img = cv.medianBlur(th_img, 7)

# visualize
cv.imshow("img", th_img)
cv.imshow("blur_img", blur_img)
cv.waitKey(0)


# Note:
# There are 2 types of thresholding - simple and adaptive

# Intuition = convert an image to binary image

# it can be used in semantic segmentation algo - segment img into diff region, we segnemt the noun from the bg  (not perfect but works for some images)
# 