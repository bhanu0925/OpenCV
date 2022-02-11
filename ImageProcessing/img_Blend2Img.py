import cv2


# multiplying the image by a scalar will increase the intensity - >  scalling

# reading the image

image1 = cv2.imread(r'.\img\eyes.jpg',0)
image1 = cv2.resize(image1,dsize=(image1.shape[1]+200,image1.shape[0]+200))
image2 = cv2.imread(r'.\img\win.jpg',0)
image2 = cv2.resize(image2,dsize=(image1.shape[1],image1.shape[0]))

image_weighted = cv2.addWeighted(src1=image1,alpha=0.25,src2=image2,beta=0.75,gamma=0)

# to blend an image the sum of alpha , beta value should sum up to 1
cv2.imshow("weighted", image_weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()