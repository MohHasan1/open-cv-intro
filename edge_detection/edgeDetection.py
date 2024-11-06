import cv2 as cv
import numpy as np
import os

# images path
img_path = os.path.join(".", "cat1.png")

# read
img = cv.imread(img_path)

# trial and error untill u get the result u one
image_edge = cv.Canny(img, 100, 200)

# optional: dilate the edge (thicker layout) - morphological transformation
d_img = cv.dilate(image_edge, np.ones((3,2), np.int8))

# erode - opposite of dilate
e_img = cv.erode(d_img, np.ones((3,2), np.int8))



# display
cv.imshow("img", img)
cv.imshow("image_edge", image_edge)
cv.imshow("dilate_img", d_img)
cv.imshow("e_img", e_img)
cv.waitKey(0)

# note:
# There are 3 different algorithms to implement edge detectorv: sobel deratived,laplace operatives, canny edge detector
