# Classe que representa uma partícula em 2D

class Particula:
    def __init__(self, x, y, vx, vy, massa):
        """
        Inicializa a particula com posição (x,y), velocidade (vx,vy) e massa.
        """
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.massa = massa

    def newton(self, fx, fy, dt):
        """
        Aplica a segunda lei de newton (F = ma) para atualizar a velocidade e posição da partícula com base nas forças fx e fy durante o intervalo de tempo dt.
        """
        ax = fx / self.massa
        ay = fy / self.massa

        # Atualiza posição com equação do MUV (x = x0 + V0.t + (a.t²)/2)
        # self.x += self.vx é o mesmo que self.x = self.x + self.vx
        self.x += self.vx * dt + 0.5 * ax * dt ** 2
        self.y += self.vy * dt + 0.5 * ay * dt ** 2

        # Atualiza velocidade
        self.vx += ax * dt
        self.vy += ay * dt
