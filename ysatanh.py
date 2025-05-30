import numpy as np

# Giriş verisi (2 boyutlu vektör)
input_x = np.array([2.5, 3.0])

# Gizli katman ağırlıkları (2x2 matris)
W1 = np.array([
    [-1.4,  2.3],
    [ 0.7, -0.5]
])

# Gizli katman bias vektörü (1x2)
b1 = np.array([1.3, 0.9])

# Çıkış katmanı ağırlıkları (2x1 matris)
W2 = np.array([
    [-0.1],
    [-0.3]
])

# Çıkış katmanı bias (1x1)
b2 = np.array([0.5])

# Aktivasyon fonksiyonu: tanh
def tanh(x):
    return np.tanh(x)

# Sinir ağı ileri besleme (forward pass) fonksiyonu
def calculate_neural_network(input_x, W1, b1, W2, b2):
    # Gizli katman: Z1 = W1 * X + b1
    z1 = np.dot(W1, input_x) + b1
    h = tanh(z1)  # Aktivasyon uygula

    # Çıkış katmanı: Z2 = W2^T * h + b2
    z2 = np.dot(W2.T, h) + b2
    output = tanh(z2)  # Aktivasyon uygula

    return h, output

# Hesaplama
hidden_layer_output, network_output = calculate_neural_network(input_x, W1, b1, W2, b2)

# Sonuçları yazdır
print("Giriş Verileri (X):", input_x)
print("Gizli Katman Ağırlıkları (W1):\n", W1)
print("Gizli Katman Biasları (b1):", b1)
print("Çıkış Katmanı Ağırlıkları (W2):\n", W2)
print("Çıkış Katmanı Biasları (b2):", b2)
print("\n--- Sinir Ağı Sonuçları ---")
print("Gizli Katman Çıkışı (h):", hidden_layer_output)
print("Ağ Çıkışı (y):", network_output.item())  # Tek bir skaler değeri yazdır
