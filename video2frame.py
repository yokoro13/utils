import os
import shutil
import cv2

video_file = "./movies/sky4.mp4"
image_dir = "./sky_/"
image_file = "%s.jpg"

offset = len(os.listdir(image_dir))

# Video to frames
i = offset
cap = cv2.VideoCapture(video_file)

num = 0

while cap.isOpened():
    flag, frame = cap.read()  # Capture frame-by-frame
    if num % 1 == 0:
        if not flag:  # Is a frame left?
            break
        cv2.imwrite(image_dir + image_file % str(i).zfill(6), frame)  # Save a frame
        print('Save', image_dir + image_file % str(i).zfill(6))
        i += 1
    num += 1

cap.release()  # When everything done, release the capture
