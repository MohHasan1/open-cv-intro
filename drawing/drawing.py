# Drawings - line, rectangle, circle, text
import cv2 as cv
import os
import colors as c

# path - if path error copy path using "copy path". (Also, remeber os.path = parent dir so, parent/chiled):
path = os.path.join(".", "drawing", "wb.png")

# read
img = cv.imread(path)

# shape
print(img.shape)

# line
cv.line(img=img, pt1=(500, 950), pt2=(1000, 850), color=c.MAGENTA, thickness=6)

# rectangle p1=upper left, p2=bottom right 
# -ve mean fill the shape
cv.rectangle(img=img, pt1=(600, 550), pt2=(1040, 800), color=c.RED, thickness=-6)

# circle
cv.circle(img=img, center=(1000, 900), radius=60, color=c.BLUE, thickness=4)

# text
cv.putText(img=img, text="This is a text", org=(1700, 1000), fontFace=5, fontScale=2, color=c.BLACK,thickness=3)

# display
cv.imshow("img", img)
cv.waitKey(0)


# note the axis:
########################### x
# 0 1 2 3 4 5 6 
# 1 
# 2
# 3
# 4
# 5
# 6
# 
# y