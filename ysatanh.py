import numpy as np

# --------------------------
# Aktivasyon Fonksiyonları
# --------------------------

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# --------------------------
# Sinir Ağı Hesaplama Fonksiyonu
# --------------------------

def calculate_neural_network(input_x, W1, b1, W2, b2, activation_hidden, activation_output):
    """
    Tek gizli katmanlı ileri beslemeli sinir ağı hesaplaması
    """
    # 1. Gizli katman hesaplaması: Z1 = W1 * X + b1
    z1 = np.dot(W1, input_x) + b1
    h = activation_hidden(z1)  # Aktivasyon uygulanıyor

    # 2. Çıkış katmanı hesaplaması: Z2 = W2^T * h + b2
    z2 = np.dot(W2.T, h) + b2
    output = activation_output(z2)  # Aktivasyon uygulanıyor

    return h, output

# --------------------------
# Ağ Parametreleri
# --------------------------

# Giriş (2 boyutlu vektör)
input_x = np.array([2.5, 3.0])

# Ağırlıklar ve biaslar
W1 = np.array([[-1.4, 2.3],
               [0.7, -0.5]])

b1 = np.array([1.3, 0.9])

W2 = np.array([[-0.1],
               [-0.3]])

b2 = np.array([0.5])

# --------------------------
# Hesaplama ve Sonuçlar
# --------------------------

# Aktivasyon fonksiyonlarını seç
activation_hidden = tanh
activation_output = tanh

# Hesapla
hidden_output, network_output = calculate_neural_network(input_x, W1, b1, W2, b2, activation_hidden, activation_output)

# --------------------------
# Sonuçları Yazdır
# --------------------------

print("==== GİRİŞ ====")
print("Giriş Verisi (X):", input_x)

print("\n==== AĞ PARAMETRELERİ ====")
print("Gizli Katman Ağırlıkları (W1):\n", W1)
print("Gizli Katman Biasları (b1):", b1)
print("Çıkış Katmanı Ağırlıkları (W2):\n", W2)
print("Çıkış Katmanı Biası (b2):", b2)

print("\n==== HESAPLAMA SONUÇLARI ====")
print("Gizli Katman Lineer Çıkışı (Z1):", np.dot(W1, input_x) + b1)
print("Gizli Katman Aktivasyon Çıkışı (h):", hidden_output)
print("Çıkış Katmanı Lineer Çıkışı (Z2):", np.dot(W2.T, hidden_output) + b2)
print("Ağ Çıkışı (y):", network_output.item())  # Tek skaler
