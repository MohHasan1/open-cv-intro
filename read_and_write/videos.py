import cv2 as cv
import os

# path
video_path = os.path.join(".", "video1.mov")

# read
video = cv.VideoCapture(video_path)

# visualize
ret = True
while ret:
    # read
    ret, frame = video.read()

    # show
    # if a frame is read successfully
    if ret:
        cv.imshow("video frame", frame)
        # how will we wait for each frame?
        # 60 frame per sec = 1/60 = 10 (0.016)
        # 25 frame per sec = 1/25 = 40 ms (0.04)
        cv.waitKey(1)

# Note:
# frame = image, ret = is the frame is successfully loaded
# Alse if we set timer = 0 -  cv.waitKey(0), the video will run we will be stuck on the first frame

# Always relase the memory - must do when we work with video
video.release()
cv.destroyAllWindows()