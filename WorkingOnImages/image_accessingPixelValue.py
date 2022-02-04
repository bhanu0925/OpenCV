import cv2

# reading the image
image = cv2.imread(filename=r'D:\iNeuron\OpenCV_A2Z\WorkingOnImages\img\Resized.jpg',flags=1)
print(image)
image[0:100,0:100]= 255
image[0:80,0:50]= [42,42,165]
print(image)

cv2.imshow('My pic', image)
cv2.imwrite(r'D:\iNeuron\OpenCV_A2Z\WorkingOnImages\img\accessPx.jpg', image)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()