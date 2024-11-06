import cv2 as cv
import os


# path
path = os.path.join(".", "cat1.png")

# read
img = cv.imread(path)

# shape
print(img.shape)

# cropping 
# recall img is stored in a numby array
# [height, width]
cropped_img = img[620: 1200, 420: 1300]

# visualize
cv.imshow("window", cropped_img)
cv.waitKey(0)