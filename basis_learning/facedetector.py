import cv2

class FaceDetector:
	def __init__(self, faceCascadePath):
		self.faceCascade = cv2.CascadeClassier(faceCascadePath)

	def detect(self, image, scaleFactor=1.1, minNeighbours=5,
		minSize=(30, 30)):
	rects = self.faceCascade.detectMultiScale(image, 
		scaleFactor=scaleFactor, minNeighbours=minNeighbours,
		minSize=minSize, flags=cv2.CASCADE_SCALE_IMAGE)
	return rects 


