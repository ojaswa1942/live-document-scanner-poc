from utils.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

video_capture = cv2.VideoCapture(0)
process_this_frame = True

while True:
	# Grab a single frame of video
	ret, frame = video_capture.read()

	if process_this_frame:
		# Process
		ratio = frame.shape[0] / 500.0
		orig = frame.copy()
		frame = imutils.resize(frame, height = 500)
		warped = orig

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (5, 5), 0)
		edged = cv2.Canny(gray, 75, 200)

		cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

		for c in cnts:
			# approximate the contour
			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.02 * peri, True)

			# if our approximated contour has four points, then we
			# can assume that we have found our screen
			flag = False
			if len(approx) == 4:
				flag = True
				screenCnt = approx
				break
		
		if flag:
			warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

		# convert the warped image to grayscale, then threshold it
		# to give it that 'black and white' paper effect
		
		# warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
		# T = threshold_local(warped, 11, offset = 10, method = "gaussian")
		# warped = (warped > T).astype("uint8") * 255


	# process_this_frame = not process_this_frame

	# Display the resulting image
	cv2.startWindowThread()
	cv2.imshow('Video', imutils.resize(warped, height = 650))
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()