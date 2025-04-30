import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('D:/Final_BonusOdevGoruntuleri/Lenna.jpg', cv2.IMREAD_GRAYSCALE)


f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)


magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)  # +1 ile log(0) hatası önlenir


rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols), np.uint8)
mask_size = 30
mask[crow - mask_size:crow + mask_size, ccol - mask_size:ccol + mask_size] = 1


fshift_filtered = fshift * mask


f_ishift = np.fft.ifftshift(fshift_filtered)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


plt.figure(figsize=(12, 8))

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Frekans Spektrumu'), plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(img_back, cmap='gray')
plt.title('Düşük Frekanslı Filtrelenmiş'), plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
