## resizing images

import cv2

# reading the image
image = cv2.imread(filename=r'.\img\nature.jpg', flags=1)
print("original size : ", image.shape)

## resizing will be in width and height formate, but shapre will be (height , width) format

new_image = cv2.resize(image,dsize=(500,300))
print("new image size : ", new_image.shape)
cv2.imwrite(r'.\img\Resized.jpg',new_image)
# displaying image
# window name
# image matrix - image varoable
cv2.imshow('My pic', new_image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()

## display image in some ration of the original image
ratio_image = cv2.resize(image,dsize=(0,0), fx=0.03,fy=0.05)
print("new image size : ", ratio_image.shape)
cv2.imshow('My pic', ratio_image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()

## display image in some ration of the original image
ratio_image = cv2.resize(image,dsize=(0,0), fx=0.3,fy=1)
print("new image size : ", ratio_image.shape)
cv2.imshow('My pic', ratio_image)



cv2.waitKeyEx(0)
cv2.destroyAllWindows()