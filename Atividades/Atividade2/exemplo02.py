# Importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from particula import Particula
import math

# Constantes
g = 9.8 # aceleração da gravidade (m/s²)
dt = 0.01 # intervalo de tempo (s)
massa = 1.0 # kg


v0 = 20  # velocidade inicial em m/s
angulos_graus = [15, 30, 45, 60, 75]  # ângulos em graus

# Cores diferentes para cada curva
cores = ['red', 'orange', 'green', 'blue', 'purple']

plt.figure(figsize=(10, 6))

for angulo, cor in zip(angulos_graus, cores):
    rad = math.radians(angulo)
    vx0 = v0 * math.cos(rad)
    vy0 = v0 * math.sin(rad)

    p = Particula(0, 0, vx0, vy0, massa)

    posicoes_x = []
    posicoes_y = []
    t = 0

    while p.y >= 0:
        posicoes_x.append(p.x)
        posicoes_y.append(p.y)

        fx = 0
        fy = -massa * g
        p.newton(fx, fy, dt)
        t += dt

    plt.plot(posicoes_x, posicoes_y, color=cor, label=f'{angulo}°')

# Plot final
plt.title('Trajetórias para Diferentes Ângulos de Lançamento')
plt.xlabel('Posição X (m)')
plt.ylabel('Posição Y (m)')
plt.legend(title="Ângulos")
plt.ylim(0)
plt.xlim(0)
plt.grid(True)
plt.show()