import cv2 as cv
import os

# path
path = os.path.join(".", "simple_operations","cat1.png")

# read
img = cv.imread(path)

# blurr (img, size of the neighbourhood = radius kind of) (x, y)
# larger the k value higher teh blurr
blurred_img = cv.blur(img, (7, 7))

g_img = cv.GaussianBlur(img, (7,7), 10)

m_img = cv.medianBlur(img, 7)

# visualize - frame
cv.imshow("image", blurred_img)
cv.imshow("g_img", g_img)
cv.imshow("m_img", m_img)
cv.waitKey(0)

# note: imp to remoce noise and blur can help us
# There are 4 functions in open cv

# intuition - loose details
# when we apply blur we can think of averages - replacing every pixels by the average of all the otehr pixels which are around it.
# The avg of all the pixels of a neighbourhood of a pixel. - high level idea

# !!diff func uses diff mathic formula to cal the avg!!