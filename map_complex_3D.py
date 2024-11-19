import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Função do mapa logístico para números complexos
def logistic_map_complex(z, r):
    return r * z * (1 - z)

# Configurações para o gráfico
width, height = 300, 300  # Tamanho reduzido para melhorar o desempenho durante a animação
re_min, re_max = -1.5, 1.5  # Intervalo do eixo real
im_min, im_max = -0.5, 0.5  # Intervalo do eixo imaginário
max_iter = 50  # Número máximo de iterações
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

# Criar o gráfico 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Criar a grade de coordenadas
X, Y = np.meshgrid(np.linspace(re_min, re_max, width), np.linspace(im_min, im_max, height))

# Plotar a superfície em 3D
surface = ax.plot_surface(X, Y, output, cmap='hot', edgecolor='none')

# Configurações do gráfico
ax.set_title('Mapa Logístico Complexo em 3D')
ax.set_xlabel('Parte Real')
ax.set_ylabel('Parte Imaginária')
ax.set_zlabel('Número de Iterações')

# Função de animação para rotacionar a visualização
def update_view(angle):
    ax.view_init(elev=10 + (angle % 90), azim=angle)

# Criar animação
ani = FuncAnimation(fig, update_view, frames=np.arange(0, 360, 2), interval=100)

plt.show()
