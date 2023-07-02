import cv2  #Importamos asi para solucionar aviso del linter
import matplotlib.pyplot as plt
import matplotlib.image as img

#Get the img matrix
image = cv2.imread("imgs/paradrop.png")
#Convert the image to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Import directly grayscale image
direct_gray_image = cv2.imread("imgs/paradrop.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', image)
cv2.waitKey(0)
