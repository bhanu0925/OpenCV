import cv2

image1 = cv2.imread(r'.\img\eyes.jpg')
image1 = cv2.resize(image1,dsize=(image1.shape[1]+200,image1.shape[0]+200))
image2 = cv2.imread(r'.\img\win.jpg')
image2 = cv2.resize(image2,dsize=(image1.shape[1],image1.shape[0]))

## dividing each pixel of an image seperately and then adding will preserve the intensity range 0 - 255

image_sub = cv2.subtract(image1,image2)
cv2.imshow("seb",image_sub)
cv2.waitKey(0)
cv2.destroyAllWindows()