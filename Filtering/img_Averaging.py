import cv2

# reading the image
image = cv2.imread(filename=r'.\img\nature.jpg')

cv2.imshow('My pic', image)

blur = cv2.blur(image,(3,3))
cv2.imshow('average blurring', blur)

blur2 = cv2.blur(image,(5,5))
cv2.imshow('average blurring', blur2)

cv2.waitKey(0)
cv2.destroyAllWindows()