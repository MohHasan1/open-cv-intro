# demo - object detection
import os
import colors as c
import cv2 as cv

# path
path = os.path.join(".", "contours", "birds.jpg")

# read
birds = cv.imread(path)

# 1. grayscale
g_birds = cv.cvtColor(src=birds, code=cv.COLOR_BGR2GRAY)

# 2. Threshold
ret, th_birds = cv.threshold(
    src=g_birds, thresh=120, maxval=255, type=cv.THRESH_BINARY_INV)

# 3. contour (2 or 3 retuns depends on teh version)
# There might be overlappimg if objexts are close
# we are going to have an array of contour and a border for each isolatetd white border
contours, hierarchy = cv.findContours(
    image=th_birds, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

# There might be noise liek contours that are noice we dont need
for cnt in contours:
    # remove noisy contours
    if cv.contourArea(contour=cnt) > 200:
        # print(cv.contourArea(contour=cnt))

        # contours
        cv.drawContours(image=birds, contours=cnt,contourIdx=-1, color=c.YELLOW, thickness=3)

        # 1. get the bounding box coordinate
        x1, y1, w, h = cv.boundingRect(array=cnt)

        # 2. boundaing box
        cv.rectangle(img=birds, pt1=(x1, y1), pt2=(x1+w,y1+h), color=c.YELLOW, thickness=3)



# view
cv.imshow("birds", birds)
cv.waitKey(0)

# note we might need to proces the image:
# grayscale -> threshold maybe -> blur maybe


# in contour we detect white isolated object. so we use THRESH_BINARY_INV
