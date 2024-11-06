import cv2 as cv
import os

# path
img_path = os.path.join(".", "cat1.png")

# read
img = cv.imread(img_path)

# read first and then work with it (like resize)
# RESIZE (img, (w, h)) -> propertion might be affected
resized_img = cv.resize(img, (650, 500))

# shape (numpy array) - (h, w)
print(img.shape)
print(resized_img.shape)

# visualize - frame
cv.imshow("image", resized_img)
cv.waitKey(0)
