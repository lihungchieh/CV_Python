from __future__ import print_function
import numpy as np 
import argparse
import cv2
from facedetector import FaceDetector 

ap = argparse.ArgumentParser()
ap.add_argument('-f','--face',required=True, 
	help='path to where the face canscade')
ap.add_argument('-i','--image',required=True, help='path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image', image)
cv2.waitKey(0)

fd = FaceDetector(args['face'])
faceRects = fd.detect(gray, scaleFactor=1.2, minNeighbours=5,minSize=(30,30))
print('I found {} face(s) in the image'.format(len(faceRects)))

for (x, y, w, h) in faceRects:
	cv2.rectangle(image, (x, y), (x+w,y+h),(0,255,0), 2)

cv2.imshow('Faces', image)
cv2.waitKey(0)