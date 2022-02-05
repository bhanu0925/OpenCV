
import cv2

# reading the image
image = cv2.imread(filename=r'.\img\Resized.jpg')

cv2.circle(image,center=(300,400),radius=105,color=432,thickness=5,lineType=1)
cv2.circle(image,center=(100,200),radius=200,color=333,thickness=4,lineType=cv2.LINE_AA)
cv2.circle(image,center=(40,300),radius=145,color=234,thickness=3,lineType=5)
cv2.circle(image,center=(345,400),radius=150,color=123,thickness=2,lineType=cv2.LINE_AA)

# displaying image5
# window name
# image matrix - image varoable
cv2.imshow('My pic', image)
cv2.imwrite(r'.\img\circle.jpg',image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()