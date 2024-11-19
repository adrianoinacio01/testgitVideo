import numpy as np
import matplotlib.pyplot as plt

# Função do mapa logístico
def logistic_map(x, r):
    return r * x * (1 - x)

# Configurações iniciais
r = 3.5  # Parâmetro de controle
x0 = 0.5  # Valor inicial
iterations = 100  # Número de iterações

# Lista para armazenar os valores de x
x_values = [x0]

# Itera o mapa logístico
for _ in range(iterations - 1):
    x_values.append(logistic_map(x_values[-1], r))

# Cria o gráfico
plt.plot(x_values, marker='o', linestyle='-', color='b')
plt.title(f'Mapa Logístico (r={r})')
plt.xlabel('Iteração')
plt.ylabel('x')
plt.grid(True)
plt.show()
