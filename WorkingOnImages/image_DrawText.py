import cv2

# reading the image
image = cv2.imread(filename=r'.\img\Resized.jpg')
cv2.putText(image,"Bhanu",org=(100,300),fontFace=cv2.FONT_ITALIC,fontScale=4,color=(3,5,23),thickness=2,lineType=3)
cv2.putText(image,"Deepak",org=(00,100),fontFace=cv2.FONT_ITALIC,fontScale=4,color=(3,5,23),thickness=2,lineType=3)
# displaying image
# window name
# image matrix - image varoable
cv2.imshow('My pic', image)
cv2.imwrite(r'.\img\text.jpg',image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()