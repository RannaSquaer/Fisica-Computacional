# Importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from particula import Particula
import math

# Constantes
g = 9.8  # aceleração da gravidade (m/s²)
dt = 0.1  # intervalo de tempo (s)
massa = 1.0  # kg

# Criando a partícula
p = Particula(0, 0, 10, 10, massa)

# Listas para armazenar os dados
tempos = []
posicoes_x = []
posicoes_y = []
velocidades_x = []
velocidades_y = []

t = 0.0

while p.y >= 0:
    # Salva os dados
    tempos.append(t)
    posicoes_x.append(p.x)
    posicoes_y.append(p.y)
    velocidades_x.append(p.vx)
    velocidades_y.append(p.vy)

    # Aplica a força da gravidade
    fx = 0
    fy = -massa * g  # Força para baixo
    p.newton(fx, fy, dt)

    # Atualiza o tempo
    t += dt

# Resultado final
print("Simulação encerrada: partícula atingiu o solo.")
print(f"Tempo total: {t:.2f} segundos")


plt.plot(posicoes_x, posicoes_y)
plt.xlabel('Posição X (m)')
plt.ylabel('Posição Y (m)')
plt.title('Trajetória da Partícula Sob Gravidade')
plt.grid(True)
plt.show()
