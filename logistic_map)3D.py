import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Função do mapa logístico
def logistic_map(x, r):
    return r * x * (1 - x)

# Configurações para o gráfico 3D
r_values = np.linspace(0.01, 2.5, 200)  # Intervalo de valores de r
iterations = 100  # Número de iterações
last_iterations = 50  # Número de iterações a serem plotadas (as últimas)
x0 = 0.5  # Valor inicial

# Preparar os dados para o gráfico
x_values = np.empty((len(r_values), last_iterations))
for i, r in enumerate(r_values):
    x = x0
    for _ in range(iterations - last_iterations):
        x = logistic_map(x, r)  # Iterações para estabilizar
    for j in range(last_iterations):
        x = logistic_map(x, r)
        x_values[i, j] = x

# Criar o gráfico 3D
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

# Plotar os pontos
for i in range(len(r_values)):
    ax.plot([r_values[i]] * last_iterations, range(iterations - last_iterations, iterations), x_values[i], 'b.')

# Configurações do gráfico
ax.set_title('Mapa Logístico em 3D')
ax.set_xlabel('r')
ax.set_ylabel('Iteração')
ax.set_zlabel('x')

# Função de animação para rotacionar o gráfico e variar a elevação
def update_view(num):
    elev = 15 + (num % 45)  # Elevação variando entre 30 e 75 graus
    azim = num  # Rotação completa de 0 a 360 graus
    ax.view_init(elev=elev, azim=azim)

# Criar animação
ani = FuncAnimation(fig, update_view, frames=np.arange(0, 360, 2), interval=100)


plt.show()

