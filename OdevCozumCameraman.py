import numpy as np
import cv2
from matplotlib import pyplot as plt


image_path = 'D:/Final_BonusOdevGoruntuleri/Cameraman.jpg'
low_pass_size = 30  


img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError(f"Görüntü bulunamadı: {image_path}")


f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)


rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.ones((rows, cols), np.uint8)
mask[crow-low_pass_size:crow+low_pass_size, ccol-low_pass_size:ccol+low_pass_size] = 0

fshift_filtered = fshift * mask
f_ishift = np.fft.ifftshift(fshift_filtered)
img_filtered = np.fft.ifft2(f_ishift)
img_filtered = np.abs(img_filtered)

plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(132)
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)  # +1 log(0) hatası için
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Fourier Spektrumu')
plt.axis('off')

plt.subplot(133)
plt.imshow(img_filtered, cmap='gray')
plt.title('Kenarları Belirgin Görüntü')
plt.axis('off')

plt.tight_layout()
plt.show()
