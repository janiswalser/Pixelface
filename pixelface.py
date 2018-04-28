import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("data/haarcascade_eye.xml")


cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)




while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#detect the face
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in faces:
		
		start = [width/2, height/2]
		amount = 6
		bigPixel = (round(w/6))
		
		startY = ((y))
 		startX = ((x))

 		# Lets go through each Pixel 
		for t in range(0,amount):
	 		for i in range(0,amount):
	 			# get the average color
				average_color = gray[ (startY + t*bigPixel):(startY + t*bigPixel + bigPixel) , (startX + i*bigPixel):(startX + i*bigPixel + bigPixel)].mean()
				# go and tint it
				gray[ (startY + t*bigPixel):(startY + t*bigPixel + bigPixel) , (startX + i*bigPixel):(startX + i*bigPixel + bigPixel) ] = average_color


	# display image 
	cv2.imshow('img', gray)

	# the way out 
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()








