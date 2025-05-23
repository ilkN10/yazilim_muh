
import numpy as np
import cv2
from matplotlib import pyplot as plt

def load_image(path):
    """Görüntüyü gri tonlamalı olarak yükler."""
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)

def fft_image(img):
    """Görüntünün FFT dönüşümünü ve merkeze kaydırılmış halini döndürür."""
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    return f, fshift

def create_low_pass_mask(shape, mask_size):
    """Belirtilen boyutlarda bir düşük geçiren filtre maskesi oluşturur."""
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow - mask_size:crow + mask_size, ccol - mask_size:ccol + mask_size] = 1
    return mask

def apply_filter(fshift, mask):
    """Fourier dönüşümüne filtre uygular."""
    return fshift * mask

def inverse_fft(fshift_filtered):
    """Filtrelenmiş görüntüyü ters Fourier ile geri döndürür."""
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    return np.abs(img_back)

def plot_results(img, magnitude_spectrum, mask, fshift_filtered, img_back):
    """Tüm adımları görselleştirir."""
    filtered_spectrum = 20 * np.log(np.abs(fshift_filtered) + 1)

    plt.figure(figsize=(15, 10))

    plt.subplot(231), plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(232), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Frekans Spektrumu'), plt.xticks([]), plt.yticks([])

    plt.subplot(233), plt.imshow(mask * 255, cmap='gray')
    plt.title('Kullanılan Maske'), plt.xticks([]), plt.yticks([])

    plt.subplot(234), plt.imshow(filtered_spectrum, cmap='gray')
    plt.title('Filtrelenmiş Spektrum'), plt.xticks([]), plt.yticks([])

    plt.subplot(235), plt.imshow(img_back, cmap='gray')
    plt.title('Düşük Frekanslı Filtrelenmiş'), plt.xticks([]), plt.yticks([])

    plt.tight_layout()
    plt.show()


# ==== Ana Akış ====
image_path = 'D:/Final_BonusOdevGoruntuleri/Lenna.jpg'
mask_size = 30  # Değiştirilebilir

img = load_image(image_path)
f, fshift = fft_image(img)
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

mask = create_low_pass_mask(img.shape, mask_size)
fshift_filtered = apply_filter(fshift, mask)
img_back = inverse_fft(fshift_filtered)

plot_results(img, magnitude_spectrum, mask, fshift_filtered, img_back)
