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

Em andamento...

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
``

## Implementação

### Arquitetura do Agente

O agente autônomo é composto por:

- **Ambiente Simulado**: Utilizamos o Gym para criar um ambiente simulado que represente a cidade e os desafios de navegação.
- **Algoritmo de Aprendizagem por Reforço**: Implementamos algoritmos como DQN (Deep Q-Network) e A2C (Advantage Actor-Critic) para treinar o agente.
- **Rede Neural**: Utilizamos PyTorch para criar e treinar uma rede neural que auxilia na tomada de decisões do agente.

### Código Principal

Os arquivos principais do projeto incluem:

- `main.py`: Código principal para iniciar e gerenciar o treinamento do agente.
- `ai.py`: Definição da arquitetura do agente, incluindo a rede neural e as funções de treinamento.
- `map.py`: Definição do ambiente simulado utilizando o Gym.

## Treinamento

O treinamento do agente é realizado em várias etapas:

1. **Inicialização do Ambiente**: Configuração do ambiente simulado.
2. **Treinamento do Agente**: Utilização de algoritmos de RL para treinar o agente a tomar decisões ótimas.
3. **Monitoramento**: Avaliação contínua do desempenho do agente durante o treinamento.
4. **Ajustes de Hiperparâmetros**: Ajustes nos parâmetros do algoritmo e da rede neural para melhorar o desempenho.

## Avaliação

Após o treinamento, o agente é avaliado em diferentes cenários para verificar:

- **Eficiência**: Capacidade de encontrar as rotas mais curtas e rápidas.
- **Segurança**: Capacidade de evitar obstáculos e seguir regras de trânsito simuladas.
- **Robustez**: Desempenho em diferentes condições de simulação.

## Conclusão

O agente autônomo demonstra a aplicação prática de técnicas de Aprendizagem por Reforço e 
Deep Learning para resolver problemas complexos de navegação e tomada de decisão. 
Os resultados mostram o potencial dessas técnicas para desenvolver sistemas autônomos eficientes e seguros.
