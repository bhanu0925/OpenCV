import cv2

# adding two images : added pixel by pixel : pixel wise operations

# reading the image

image1 = cv2.imread(r'.\img\eyes.jpg')
image1 = cv2.resize(image1,dsize=(image1.shape[1]+200,image1.shape[0]+200))
image2 = cv2.imread(r'.\img\win.jpg')
image2 = cv2.resize(image2,dsize=(image1.shape[1],image1.shape[0]))

## dividing each pixel of an image seperately and then adding will preserve the intensity range 0 - 255

sumImg = image1//2 + image2//2
cv2.imshow("summed image",sumImg)

## averaging the images will exceed the image intensity and rounded off to 255 if > 255, and 0 if > 0

avgImg = (image1 + image2) // 2
cv2.imshow("Averaged image", avgImg)


cv2.waitKey(0)
cv2.destroyAllWindows()