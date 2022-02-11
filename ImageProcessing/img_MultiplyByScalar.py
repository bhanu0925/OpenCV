import cv2
import matplotlib.pyplot as plt

# multiplying the image by a scalar will increase the intensity - >  scalling

# reading the image

image1 = cv2.imread(r'.\img\eyes.jpg',0)
image1 = cv2.resize(image1,dsize=(image1.shape[1]+200,image1.shape[0]+200))
image2 = cv2.imread(r'.\img\win.jpg',0)
image2 = cv2.resize(image2,dsize=(image1.shape[1],image1.shape[0]))

## dividing each pixel of an image seperately and then adding will preserve the intensity range 0 - 255
print(image1)

mulImg = image1 * 0.5
mulImg=mulImg.astype('uint8')

plt.subplot(121)
plt.imshow(mulImg)
plt.title('eyes')
plt.show()

#cv2.imshow("1",mulImg)

## averaging the images will exceed the image intensity and rounded off to 255 if > 255, and 0 if > 0
mulImg2 = image1 * 1.5
mulImg2=mulImg2.astype('uint8')
#cv2.imshow("A2", mulImg2)

plt.subplot(121)
plt.imshow(mulImg2)
plt.title('win')

plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()