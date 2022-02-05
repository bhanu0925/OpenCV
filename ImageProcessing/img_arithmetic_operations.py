import cv2

# adding two images : added pixel by pixel : pixel wise operations

# reading the image
image1 = cv2.imread(r'.\img\nature.jpg')
image1 = cv2.resize(image1,dsize=(image1.shape[1]+200,image1.shape[0]+200))
image2 = cv2.imread(r'.\img\cute2.jpg')
#image2 = cv2.imread(r'.\img\cute1.jpg')
image2 = cv2.resize(image2,dsize=(image1.shape[1],image1.shape[0]))

image_add = cv2.add(image1,image2)
image_sub = cv2.subtract(image1,image2)
image_mul = cv2.multiply(image1,image2)
image_div = cv2.divide(image1,image2,scale=200)
image_weighted = cv2.addWeighted(src1=image1,alpha=1,src2=image2,beta=1.0,gamma=1)

img = [image_add,image_sub,image_mul,image_div,image_weighted]
for pic in img:
    cv2.imshow('My pic', pic)
    cv2.waitKeyEx(0)
    cv2.destroyAllWindows()