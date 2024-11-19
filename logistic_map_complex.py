import numpy as np
import matplotlib.pyplot as plt

# Função do mapa logístico para números complexos
def logistic_map_complex(z, r):
    return r * z * (1 - z)

# Configurações para o gráfico
width, height = 1000, 1000  # Tamanho da imagem
re_min, re_max = -0.5, 0.5  # Intervalo do eixo real
im_min, im_max = -0.5, 0.5  # Intervalo do eixo imaginário
max_iter = 25  # Número máximo de iterações
r = 0.8 + 0.6j  # Parâmetro de controle complexo

# Criar uma matriz para armazenar os valores de iteração
output = np.zeros((height, width))

# Gerar o conjunto baseado no mapa logístico complexo
for x in range(width):
    for y in range(height):
        real = re_min + (x / width) * (re_max - re_min)
        imag = im_min + (y / height) * (im_max - im_min)
        z = complex(real, imag)
        for n in range(max_iter):
            z = logistic_map_complex(z, r)
            if abs(z) > 2:
                output[y, x] = n
                break

# Plotar o conjunto
plt.figure(figsize=(10, 10))
plt.imshow(output, cmap='hot', extent=[re_min, re_max, im_min, im_max])
plt.colorbar()
plt.title('Mapa Logístico Complexo')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.show()
