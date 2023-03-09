import cv2

vid = cv2.VideoCapture(1)

while(True):

	ret, frame = vid.read()
	frame = cv2.resize(frame, None, fx=0.4, fy=0.6)
	cv2.imshow('frame',frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
vid.release()
cv2.destroyAllWindows()