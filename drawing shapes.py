import cv2
import numpy as np

# Create a black image
img = np.zeros((1920, 1080, 3), dtype=np.uint8)

# Rectangle in BGR format
cv2.rectangle(img, pt1=(100, 100), pt2=(300, 400), color=(255, 0, 0), thickness=-1)

# Circle
cv2.circle(img, center=(100, 400), radius=80, color=(0, 0, 255), thickness=-1)

# Line
cv2.line(img, pt1=(0, 0), pt2=(512, 512), thickness=2, color=(0, 255, 0))

# Text
cv2.putText(img, text='Hello', org=(400, 400), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
            fontScale=4, color=(0, 255, 255), thickness=2, lineType=cv2.LINE_AA)


# Display the image
cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
