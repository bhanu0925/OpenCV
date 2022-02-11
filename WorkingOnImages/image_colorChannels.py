import cv2

# reading the image
image = cv2.imread(filename=r'.\img\nature.jpg')
print(type(image))
imgRed = image[:,:,0]
imgGreen = image[:,:,1]
print(imgGreen.shape)
imgBlue = image[:,:,2]

#cv2.line(imgGreen,pt1=(2,5),pt2=(140,50),color=123,thickness=10,lineType=4)
cv2.imshow('red', imgRed)
cv2.imshow('Green', imgGreen)
cv2.imshow('blue', imgBlue)


## color image
cv2.imshow('My pic', image[120:150,40:200])
## grey image
image2 = cv2.imread(filename=r'.\img\nature.jpg',flags=0)
cv2.imshow('My pic2', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()