import cv2
import cv2.colored_kinfu
import numpy as np

# Read an image
img = cv2.imread('cody-scott-milewski-aCnkRlBD0i4-unsplash.jpg')
# orignal image size
# (2349,4176)
# img_resize = cv2.resize(img,(1920,1080))

img_resize = cv2.resize(img,(img.shape[1]//2,img.shape[0//2]))
cv2.imshow('window',img_resize)

cv2.waitKey(0)