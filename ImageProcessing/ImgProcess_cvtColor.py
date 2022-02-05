import cv2

# reading the image
image = cv2.imread(r'.\img\resized.jpg')

cvt_img = cv2.cvtColor(src=image,code=cv2.COLOR_BGR2GRAY)
#cvt_img = cv2.cvtColor(src=image,code=cv2.COLOR_BGR2LAB)
# displaying image
# window name
# image matrix - image variable
cv2.imshow('My pic', cvt_img)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()