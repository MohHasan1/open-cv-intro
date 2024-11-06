import cv2 as cv
import os

# images path
img_path = os.path.join(".", "cat1.png")
save_img_path = os.path.join(".", "cat1_out.png")

# read image - pc to cv
img = cv.imread(img_path)

# write image - cv to pc
cv.imwrite(save_img_path, img)

# visualize image - opens a window
cv.imshow("image frame", img)
cv.waitKey(0)  # wait till a btn is pressed

# 0 - indefinite
# 5000 ms - 5 sec
