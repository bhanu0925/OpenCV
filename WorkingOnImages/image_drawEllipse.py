
import cv2

# reading the image
image = cv2.imread(filename=r'.\img\Resized.jpg')

cv2.ellipse(image,center=(200,150),axes=(100,150),angle=0,startAngle=0,endAngle=360,color=342,thickness=3,lineType=4)
cv2.ellipse(image,center=(400,350),axes=(70,50),angle=60,startAngle=0,endAngle=180,color=(0,0,453),thickness=4,lineType=4)

# displaying image5
# window name
# image matrix - image varoable
cv2.imshow('My pic', image)
cv2.imwrite(r'.\img\ellipse.jpg',image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()