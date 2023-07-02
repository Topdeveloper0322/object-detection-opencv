# IMPORTANT: BEEN IN ENVIRONMENT WITH cv2, numpy and matplotlib installed.
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('/home/betegon/Siali/jupyter_notebooks/imgs/69.jpeg')
image_copy = image.copy()
# BGR to RGB
#image_BGR = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
image_gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

while True:
	cv2.imshow('asjndwfjasdf', image)
	k = cv2.waitKey(0)
	if k == 27:         # wait for ESC key to exit
		break	

cv2.destroyAllWindows()
