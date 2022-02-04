import cv2

# reading the image
image = cv2.imread(filename=r'D:\iNeuron\OpenCV_A2Z\WorkingOnImages\img\Resized.jpg', flags=1)
print(image)
print("original size : ", image.shape)

## writing on the image
resized = cv2.resize(image,dsize=(200,300))
cv2.imshow('My pic', resized)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()

## read in grey scale
image = cv2.imread(filename=r'D:\iNeuron\OpenCV_A2Z\WorkingOnImages\img\Resized.jpg', flags=0)
print(image)  ## displayes 2D array, 0-255
print(image[0])