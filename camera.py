#!/usr/bin/env python3
# pylint: disable=missing-module-docstring

import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret or cv.waitKey(1) == ord("q"):
        break
    cv.imshow("Press `q` to quit", frame)

cap.release()
cv.destroyAllWindows()
