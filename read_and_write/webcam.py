import cv2 as cv
import os

# read webcam
# we have webcam id single (0), multiple (0,1, ..)
# 1 webcam most prob # = 0 (default)
# 2 webcam most prob # = 0 and 1
webcam = cv.VideoCapture(0)

while True:
    # read
    ret, frame = webcam.read()
    # show
    cv.imshow("webcam", frame)
    # wait
    # Check if the 'q' key is pressed to exit (optional)
    if cv.waitKey(40) & 0xFF == ord("q"):
        break

webcam.release()
cv.destroyAllWindows()


