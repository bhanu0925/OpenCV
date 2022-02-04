import cv2

# reading the image
image = cv2.imread(filename=r'D:\iNeuron\OpenCV_A2Z\WorkingOnImages\img\Resized.jpg')


cv2.rectangle(image,pt1=(200,150),pt2=(160,250),color=342,thickness=3,lineType=4)


# displaying image5
# window name
# image matrix - image varoable
cv2.imshow('My pic', image)
cv2.imwrite(r'D:\iNeuron\OpenCV_A2Z\WorkingOnImages\img\rectangle.jpg',image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()