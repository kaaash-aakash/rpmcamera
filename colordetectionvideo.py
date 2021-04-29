# Python code for Multiple Color Detection


import numpy as np
import cv2


# Capturing video through webcam
# webcam = cv2.VideoCapture(0)
file_path = r'res/Fan speed-3 1080p 60fps.mp4'
# file_path = r'res/fidget.mp4'

cap = cv2.VideoCapture(file_path)

frame_no = 0
# Start a while loop
while(1):
	frame_no+=1
	# Reading the video from the
	# webcam in image frames
	_, imageFrame = cap.read()
	# _, imageFrame = webcam.read()

	# Convert the imageFrame in
	# BGR(RGB color space) to
	# HSV(hue-saturation-value)
	# color space
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

	# Set range for red color and
	# define mask

	# Range for lower red
	lower_red = np.array([0,120,70])
	upper_red = np.array([10,255,255])
	mask1 = cv2.inRange(hsvFrame, lower_red, upper_red)

	# Range for upper range
	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])
	mask2 = cv2.inRange(hsvFrame,lower_red,upper_red)

	red_mask = mask1+mask2
	# red_lower = np.array([60, 20, 30], np.uint8)
	# red_upper = np.array([80, 40, 50], np.uint8)
	# red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

	# Set range for green color and
	# define mask
	green_lower = np.array([25, 52, 72], np.uint8)
	green_upper = np.array([102, 255, 255], np.uint8)
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

	# Set range for blue color and
	# define mask
	blue_lower = np.array([94, 80, 2], np.uint8)
	blue_upper = np.array([120, 255, 255], np.uint8)
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
	
	# Morphological Transform, Dilation
	# for each color and bitwise_and operator
	# between imageFrame and mask determines
	# to detect only that particular color
	kernal = np.ones((5, 5), "uint8")
	
	# For red color
	red_mask = cv2.dilate(red_mask, kernal)
	res_red = cv2.bitwise_and(imageFrame, imageFrame,
							mask = red_mask)
	
	# For green color
	green_mask = cv2.dilate(green_mask, kernal)
	res_green = cv2.bitwise_and(imageFrame, imageFrame,
								mask = green_mask)
	
	# For blue color
	blue_mask = cv2.dilate(blue_mask, kernal)
	res_blue = cv2.bitwise_and(imageFrame, imageFrame,
							mask = blue_mask)

	# Creating contour to track red color
	contours, hierarchy = cv2.findContours(red_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 200):

			(x,y),radius = cv2.minEnclosingCircle(contour)
			center = (int(x),int(y))
			radius = int(radius)
			imageFrame = cv2.circle(imageFrame,center,radius,(0,255,0),2)

			# x, y, w, h = cv2.boundingRect(contour)
			# imageFrame = cv2.rectangle(imageFrame, (x, y),
			# 						(x + w, y + h),
			# 						(0, 0, 255), 2)

			print(f"frame no: {frame_no}, center{center}")
			
			cv2.putText(imageFrame, "Red Colour", (int(x)+radius, int(y)+radius),
						cv2.FONT_HERSHEY_SIMPLEX, 1.0,
						(0, 0, 255))	

	# Creating contour to track green color
	contours, hierarchy = cv2.findContours(green_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 200):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 255, 0), 2)
			
			cv2.putText(imageFrame, "Green Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX,
						1.0, (0, 255, 0))

	# Creating contour to track blue color
	contours, hierarchy = cv2.findContours(blue_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 200):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(255, 0, 0), 2)
			
			cv2.putText(imageFrame, "Blue Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX,
						1.0, (255, 0, 0))
			
	# Program Termination
	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break
