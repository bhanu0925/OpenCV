import cv2
import numpy as np
from skimage.util import random_noise

image2 = cv2.imread(r'.\img\win.jpg',0)
#image2 = cv2.resize(image2,dsize=(image1.shape[1],image1.shape[0]))
gauss = np.random.normal(0,.8,image2.size)
imgNoise = gauss.reshape(image2.shape[0],image2.shape[1]).astype('uint8')
# Add the Gaussian noise to the image


imgAddNoise = cv2.add(image2,imgNoise)
cv2.imshow("add with noise",imgAddNoise)

### using skimg


# Load the image
#img = cv2.imread("D:/downloads/opencv_logo.PNG")
img = cv2.imread(r'.\img\fruits.jpg')

# Add salt-and-pepper noise to the image.
noise_img = random_noise(img, mode='s&p', amount=0.3)

# The above function returns a floating-point image
# on the range [0, 1], thus we changed it to 'uint8'
# and from [0,255]
noise_img = np.array(255 * noise_img, dtype='uint8')

# Display the noise image
cv2.imshow('blur', noise_img)


cv2.waitKey(0)
cv2.destroyAllWindows()