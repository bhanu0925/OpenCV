import cv2

# reading the image
image = cv2.imread(filename=r'.\img\Resized.jpg')

## we do not have any function to draw circle
cv2.line(image,pt1=(200,150),pt2=(160,250),color=342,thickness=3,lineType=1)
cv2.line(image,pt1=(160,250),pt2=(400,310),color=564,thickness=3,lineType=4)
cv2.line(image,pt1=(400,310),pt2=(200,150),color=37,thickness=3,lineType=3)

x = (200+160+400)//3
y = (150+250+310)//3
cv2.circle(image,center=(x,y),radius=15,color=(5,3,245),thickness=-1,lineType=cv2.LINE_AA)
# displaying image5
# window name
# image matrix - image varoable
cv2.imshow('My pic', image)
cv2.imwrite(r'.\img\triangle.jpg',image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()