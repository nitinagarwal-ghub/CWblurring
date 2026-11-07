import cv2

image = cv2.imread("pika.png")

cv2.imshow('Original Image', image)
cv2.waitKey(0)

#Gassian Blur - smooths out photo
Gaussian = cv2.GaussianBlur(image, (15,15), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

#Median Blur - smooths out with dots
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

#Bilateral Blur - only sharp edges preserved
bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()