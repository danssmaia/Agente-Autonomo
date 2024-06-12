# Agente Autônomo

Este projeto faz parte do curso **"Aprendizagem por Reforço com Deep Learning, PyTorch e Python"** 
e tem como objetivo desenvolver um modelo de entregador autônomo utilizando técnicas de 
Aprendizagem por Reforço (Reinforcement Learning) e Deep Learning com a biblioteca PyTorch.

## Objetivos do Projeto

1. **Desenvolver um agente autônomo**: Criar um entregador que possa tomar decisões 
de forma autônoma para realizar entregas em uma cidade simulada.
2. **Aplicar técnicas de Aprendizagem por Reforço**: Utilizar algoritmos de RL para treinar o 
agente a navegar pelo mapa, evitando obstáculos e encontrando as rotas mais eficientes entre duas pontas.
3. **Implementar Deep Learning com PyTorch**: Utilizar a biblioteca PyTorch para implementar e 
treinar redes neurais que suportem o aprendizado do agente.
4. **Avaliar o desempenho do agente**: Testar o agente em cenários simulados e avaliar seu 
desempenho em termos de eficiência e segurança.

## Estrutura do Projeto

- `agent.kv`: Código com a configuração de exibição do agente e dos 3 sensores.
- `ai.py`: Definição da arquitetura do agente, incluindo a rede neural e as funções de treinamento.
- `map.py`: Definição do ambiente simulado utilizando o Kivy.


## Configuração do Ambiente

### Requisitos

- Python 3.8
- PyTorch
- Kivy

### Passos para Configuração

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/entregador-autonomo.git
    cd entregador-autonomo
    ```
2. **Instalar bibliotecas**
```
### Install PyTorch CPU version
conda install pytorch cpuonly -c pytorch

#### Install Matplotlib
conda install matplotlib

###Install Kivy
conda install -c conda-forge kivy
```

## Implementação

### Arquitetura do Agente

O agente autônomo é composto por:

- **Ambiente Simulado**: Uso do Kivy para criar um ambiente simulado que represente o mapa, os objetivos e os desafios de navegação.
- **Algoritmo de Aprendizagem por Reforço**: Implementação do algoritmo DQN (Deep Q-Network) para treinar o agente.
- **Rede Neural**: Uso PyTorch para criar e treinar uma rede neural que auxilia na tomada de decisões do agente.


## Treinamento

O treinamento do agente é realizado em várias etapas:

1. **Inicialização do Ambiente**: Configuração do ambiente simulado.
2. **Implementação de Obstaculos**: No ambiente é possível desenhar obstaculos representados por areia, não impede a movimentação do agente, porém atrapalha ele.
3. **Treinamento do Agente**: Utilização de algoritmos de RL para treinar o agente a tomar decisões ótimas.
4. **Monitoramento**: Avaliação contínua do desempenho do agente durante o treinamento.
5. **Ajustes de Hiperparâmetros**: Ajustes nos parâmetros do algoritmo e da rede neural para melhorar o desempenho, através da equação de Bellman.


## Conclusão

O agente autônomo demonstra a aplicação prática de técnicas de Aprendizagem por Reforço e 
Deep Learning para resolver problemas complexos de navegação e tomada de decisão. 
Os resultados mostram o potencial dessas técnicas para desenvolver sistemas autônomos eficientes e seguros.
