# Criação do mapa e do agente autônomo

# Importação das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

# Importação da IA que está no arquivo ai.py
from ai import Dqn

# Não permite adicionar um ponto vermelho no cenário quando é clicado com o botão direito do mouse
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# As variáveis last_x e last_y são usadas para manter na memória o último ponto quando desenhamos areia no mapa
last_x = 0
last_y = 0
n_points = 0 # Número total de pontos do último desenho
length = 0 # Tamanho do último desenho

# Criamos um objeto que chamamos de brain (cérebro), que contém a rede neural que retorna o valor de Q
brain = Dqn(5,3,0.9) # 5 entradas (sensores + direção), 3 saídas e valor de gamma
action2rotation = [0,20,-20] # action = 0 => sem rotação, action = 1 => rotaciona 20 graus, action = 2 => rotaciona -20 graus
last_reward = 0 # inicialização da última recompensa
scores = [] # inicialização do valor médio das recompensas (sliding window) com relação ao tempo

# Inicialização do mapa
first_update = True # usado para inicializar o mapa somente uma vez
def init():
    global sand # a areia é representada por um vetor que possui a mesma quantidade de pixels que a interface completo - 1 se tem areia e 0 se não tem areia
    global goal_x # coordenada x do objetivo (para onde o agente vai, do aeroporto para o centro ou o contrário)
    global goal_y # coordenada y do objetivo (para onde o agente vai, do centro para o aeroporto ou o contrário)
    global first_update 
    sand = np.zeros((longueur,largeur)) # inicialização da areia somente com zeros
    goal_x = 20 # o objetivo a alcançar é o canto superior esquerdo do mapa (é 20 e não zero porque o agente ganha recompensa negativa se tocar a parede)
    goal_y = largeur - 20 # largura - 20
    first_update = False # usado para inicializar o mapa somente uma vez

# Inicialização da última distância que indica a distância até o destino
last_distance = 0

# Criação da classe do agente 
class Agent(Widget):
    
    angle = NumericProperty(0) # inicialização do ângulo do agente
    rotation = NumericProperty(0) # inicialização da última rotação do agente (depois de uma ação, o agente faz uma rotação de 0, 20 ou -20 graus)
    velocity_x = NumericProperty(0) # inicialização da coordenada de velocidade x
    velocity_y = NumericProperty(0) # inicialização da coordenada de velocidade y
    velocity = ReferenceListProperty(velocity_x, velocity_y)  # vetor com a velocidade x e y
    sensor1_x = NumericProperty(0) # inicialização da coordenada x do primeiro sensor (frente)
    sensor1_y = NumericProperty(0) # inicialização da coordenadao y do primeiro sensor (frente)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y) # primeiro sensor
    sensor2_x = NumericProperty(0) # inicialização da coordenada x do segundo sensor (30 graus para a esquerda)
    sensor2_y = NumericProperty(0) # inicialização da coordenada y do segundo sensor (30 graus para a esquerda)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y) # segundo sensor
    sensor3_x = NumericProperty(0) # inicialização da coordenada x do terceiro sensor (30 graus para a direita)
    sensor3_y = NumericProperty(0) # inicialização da coordenada y do terceiro sensor (30 graus para a direita)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y) # terceiro sensor
    signal1 = NumericProperty(0) # inicialização do sinal recebido pelo sensor 1
    signal2 = NumericProperty(0) # inicialização do sinal recebido pelo sensor 2
    signal3 = NumericProperty(0)  # inicialização do sinal recebido pelo sensor 3

    def move(self, rotation):
        self.pos = Vector(*self.velocity) + self.pos # atualiza a posição do agente de acordo com sua última posição e velocidade
        self.rotation = rotation # busca a rotação do agente
        self.angle = self.angle + self.rotation # atualiza o ângulo
        self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos # atualiza a posição do sensor 1
        self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos # atualiza a posição do sensor 2
        self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos # atualiza a posição do sensor 3
        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400. # calcula o sinal recebido do sensor 1 (densidade de areia ao redor do sensor 1)
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400. # calcula o sinal recebido do sensor 1 (densidade de areia ao redor do sensor 2)
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400. # calcula o sinal recebido do sensor 1 (densidade de areia ao redor do sensor 3)
        if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10: # se o sensor 1 saiu do mapa
            self.signal1 = 1. # sensor 1 detecta areia
        if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10: # se o sensor 2 saiu do mapa
            self.signal2 = 1. # sensor 2 detecta areia
        if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10: # se o sensor 3 saiu do mapa
            self.signal3 = 1. # sensor 3 detecta areia

class Ball1(Widget): # sensor 1 
    pass
class Ball2(Widget): # sensor 2 
    pass
class Ball3(Widget): # sensor 3 
    pass

# Criação da classe para "jogar" 
class Game(Widget):

    agent = ObjectProperty(None) # busca o objeto agente do arquivo kivy
    ball1 = ObjectProperty(None) # busca o objeto sensor 1 do arquivo kivy
    ball2 = ObjectProperty(None) # busca o objeto sensor 2 do arquivo kivy
    ball3 = ObjectProperty(None) # busca o objeto sensor 3 do arquivo kivy

    def serve_agent(self): # inicia o agente quando executamos a aplicação
        self.agent.center = self.center # posição inicial do agente no centro do maps
        self.agent.velocity = Vector(1, 0) # o agente começa se movendo na horizontal e com velocidade 6

    def update(self, dt): # função que atualiza todas as variáveis a cada tempo t, quando chega em um novo estado (pega novos valores dos sensores)
        # especificações das variáveis globais
        global brain
        global last_reward
        global scores
        global last_distance
        global goal_x
        global goal_y
        global longueur
        global largeur

        longueur = self.width # largura do mapa (horizontal)
        largeur = self.height # altura do mapa (vertical)
        if first_update: # inicialização do mapa somente uma vez
            init()

        xx = goal_x - self.agent.x # diferença da coordenada x entre o objetivo e onde o agente está agora
        yy = goal_y - self.agent.y # # diferença da coordenada y entre o objetivo e onde o agente está agora
        orientation = Vector(*self.agent.velocity).angle((xx,yy))/180. # direção do agente com relação ao objetivo (se o agente está apontando perfeitamente para o objetivo a orientação é igual a zero
        last_signal = [self.agent.signal1, self.agent.signal2, self.agent.signal3, orientation, -orientation] # esse é o vetor de entrada, composto por três sinais dos sensores mais a orientação positiva e negativa
        action = brain.update(last_reward, last_signal) # a rede neural vai indiagent a próxima ação
        scores.append(brain.score()) # adiciona os valores das recompensas (média das 1000 últimas recompensas - sliding window)
        rotation = action2rotation[action] # converte a ação atual (0, 1 or 2) nos ângulos de rotação (0°, 20° ou -20°)
        self.agent.move(rotation) # move o agente baseado na rotação
        distance = np.sqrt((self.agent.x - goal_x)**2 + (self.agent.y - goal_y)**2) # calcula a nova distância entre o agente e o objetivo
        self.ball1.pos = self.agent.sensor1 # atualiza a posição do sensor 1
        self.ball2.pos = self.agent.sensor2 # atualiza a posição do sensor 2
        self.ball3.pos = self.agent.sensor3 # atualiza a posição do sensor 3

        if sand[int(self.agent.x),int(self.agent.y)] > 0: # se o agente está na areia
            self.agent.velocity = Vector(1, 0).rotate(self.agent.angle) # diminui a velocidade de 6 para 1
            last_reward = -1 # ganha uma recompensa negativa
        else: # caso contrário, se não estiver na areia
            self.agent.velocity = Vector(6, 0).rotate(self.agent.angle) # mantém a velocidade padrão de 6
            last_reward = -0.2 # ganha uma recompensa negativa pequena
            if distance < last_distance: # caso esteja chegando no objetivo
                last_reward = 0.1 # ganha uma pequena recompensa positiva

        if self.agent.x < 10: # se o agente está no canto esquerdo
            self.agent.x = 10 # posiciona o agente perto da parede
            last_reward = -1 # ganha recompensa negativa
        if self.agent.x > self.width - 10: # se o agente está no canto direito
            self.agent.x = self.width - 10
            last_reward = -1
        if self.agent.y < 10: # se o agente está na borda inferior 
            self.agent.y = 10
            last_reward = -1
        if self.agent.y > self.height - 10: # se o agente está na borda superior
            self.agent.y = self.height - 10
            last_reward = -1

        if distance < 100: # quando o agente chega no objetivo
            # o objetivo muda para o canto inferior direito (e vice-versa), atualizando x e y
            goal_x = self.width-goal_x 
            goal_y = self.height-goal_y 
        
        # Desenha o objetivo
        self.canvas.after.clear()
        with self.canvas.after:
            Color(0, 1, 0, 1) # cor verde
            Ellipse(pos=(goal_x - 10, goal_y - 10), size=(30, 30))
        
        # Atualiza a distância para o objetivo
        last_distance = distance
