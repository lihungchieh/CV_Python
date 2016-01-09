import numpy as np 
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)

shifted = imutils.translate(image, 25, 50)
# cv2.imshow('Shifted Down and Right', shifted)
# cv2.waitKey(0)

shifted = imutils.translate(image, -25, -50)
# cv2.imshow('Shifted Up and Left', shifted)
# cv2.waitKey(0)

rotated = imutils.rotate(image, 45)
# cv2.imshow('Rotated 45 degree', rotated)
# cv2.waitKey(0)

resized = imutils.resize(image, height=150)
# cv2.imshow('Resized to height 150', resized)
# cv2.waitKey(0)

flipped = cv2.flip(image, 1)
# cv2.imshow('Flipped Horizontally', flipped)
# cv2.waitKey(0)

flipped = cv2.flip(image, 0)
# cv2.imshow('Flipped Vertically', flipped)
# cv2.waitKey(0)

flipped = cv2.flip(image, -1)
# cv2.imshow('Flipped Horizonally and Vertically', flipped)
# cv2.waitKey(0)

cropped = image[30:120, 240:335]
# cv2.imshow('T-Rex Face', cropped)
# cv2.waitKey(0)

M = np.ones(image.shape, dtype='uint8')*100
added = cv2.add(image, M)
cv2.imshow('Added', added)

M = np.ones(image.shape, dtype='uint8')*50
subtrated = cv2.subtract(image, M)
cv2.imshow('Subtrated', subtrated)
cv2.waitKey(0)




