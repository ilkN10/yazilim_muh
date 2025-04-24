import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('D:/Final_BonusOdevGoruntuleri/Lenna.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)


rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

fshift = fshift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Gürültüsü Azaltılmış Görüntü'), plt.xticks([]), plt.yticks([])
plt.show()
