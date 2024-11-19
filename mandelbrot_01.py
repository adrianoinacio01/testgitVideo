import numpy as np
import matplotlib.pyplot as plt

# Função para calcular o conjunto de Mandelbrot
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

# Configurações da imagem
width, height = 1000, 1000  # Tamanho da imagem
re_min, re_max = -2.0, 1.0  # Intervalo do eixo real
im_min, im_max = -1.5, 1.5  # Intervalo do eixo imaginário
max_iter = 100  # Número máximo de iterações

# Criar uma matriz para armazenar os valores de iteração
mandelbrot_set = np.zeros((height, width))

# Gerar o conjunto de Mandelbrot
for x in range(width):
    for y in range(height):
        real = re_min + (x / width) * (re_max - re_min)
        imag = im_min + (y / height) * (im_max - im_min)
        c = complex(real, imag)
        mandelbrot_set[y, x] = mandelbrot(c, max_iter)

# Plotar o conjunto de Mandelbrot
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_set, cmap='hot', extent=[re_min, re_max, im_min, im_max])
plt.colorbar()
plt.title('Conjunto de Mandelbrot')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.show()
