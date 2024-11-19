import numpy as np
import matplotlib.pyplot as plt

# Função do mapa logístico
def logistic_map(x, r):
    return r * x * (1 - x)

# Criação do diagrama de bifurcação com menos pontos
r_values = np.linspace(1.5, 3.9, 100)  # Intervalo de valores de r menor
last_iterations = 50  # Número de iterações a serem plotadas (as últimas)
x0 = 0.5  # Valor inicial

plt.figure(figsize=(10, 6))

for r in r_values:
    x = x0
    for _ in range(50):  # Iterações para estabilizar
        x = logistic_map(x, r)
    for _ in range(last_iterations):
        x = logistic_map(x, r)
        plt.plot(r, x, ',k', alpha=0.2)  # Ponto no diagrama de bifurcação

plt.title('Diagrama de Bifurcação')
plt.xlabel('Taxa de Crescimento (r)')
plt.ylabel('População')
plt.ylim(0, 1)
plt.grid(True)

plt.show()
