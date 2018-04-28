
# Pixelface

![](https://github.com/janiswalser/Pixelface/blob/master/assets/face.gif)

It catches all faces and convert it in a Grid of Rects which are tinted with the average color of the captured video.

# Usage
Run the Python script and enjoy your pixeled face. 


# Face Detection

The face detection runs with OpenCV using Haar Cascades (https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html)

# Content

**1.)** Import

```
import cv2
import numpy as np
```

**2.)** Capture your Webcame

```
cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
```

**3.)** Add Magic

```
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
```


![](https://github.com/janiswalser/Pixelface/blob/master/assets/faces.gif)

You can also easily change the input!

# Change Source

**1.)** Video

```
cap = cv2.VideoCapture('name.format')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
```

**3.)** Picture

```
cap = cv2.imread('name.png',cv2.IMREAD_COLOR)
height = np.size(cap, 0)
width = np.size(cap, 1)
```

