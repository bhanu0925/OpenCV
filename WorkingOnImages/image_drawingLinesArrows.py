import cv2

# reading the image
image = cv2.imread(filename=r'D:\iNeuron\OpenCV_A2Z\WorkingOnImages\img\Resized.jpg')

cv2.line(image,pt1=(2,5),pt2=(140,50),color=123,thickness=10,lineType=4)
cv2.line(image,pt1=(300,5),pt2=(140,300),color=243,thickness=10,lineType=10)
cv2.line(image,pt1=(300,5),pt2=(140,300),color=23,thickness=2,lineType=2)

cv2.arrowedLine(image,pt1=(100,100),pt2=(200,60),color=189,thickness=3,line_type=4,tipLength=1)
cv2.arrowedLine(image,pt1=(400,500),pt2=(400,350),color=39,thickness=5,line_type=6,tipLength=1)
# displaying image5
# window name
# image matrix - image varoable
cv2.imshow('My pic', image)
cv2.imwrite(r'D:\iNeuron\OpenCV_A2Z\WorkingOnImages\img\drawlineArrow.jpg',image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()