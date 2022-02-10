import cv2

# reading the image
image = cv2.imread(filename=r'.\img\cute1.jpg')
cv2.imshow('My pic', image)
image2 = cv2.flip(image,0)
cv2.imshow('flipped', image2)
#cv2.imwrite(r'.\img\flip.jpg',image)

cv2.waitKey(0)
cv2.destroyAllWindows()