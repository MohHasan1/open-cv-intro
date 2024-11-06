import cv2 as cv
import os

# path
path = os.path.join(".", "th1.webp")

# read
img = cv.imread(path)

# convert to gayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# threshold - simple - not so efficient
# ret, th_img = cv.threshold(gray_img, 100, 255, cv.THRESH_BINARY)

# adaptive threshold - cv will automatically computethe threshold - hover over teh fun to teh arg
th_img = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21 , 30)
# we will not have one thresh hold but many different threshold, ideal threshold for a specific region
# we can think of sliding window, a small section and a ideal threshold for the threshold


# remove noise - blur (more clear)
# blur_img = cv.medianBlur(th_img, 7)

# visualize
cv.imshow("img", th_img)
# cv.imshow("blur_img", blur_img)
cv.waitKey(0)


# Note:
# There are 2 types of thresholding - simple and adaptive

# Intuition = convert an image to binary image

# it can be used in semantic segmentation algo - segment img into diff region, we segnemt the noun from the bg  (not perfect but works for some images)


# ocr will now be able to read it better