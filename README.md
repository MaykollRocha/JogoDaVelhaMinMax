# Jogo da Velha com IA (Minimax + Poda Alfa-Beta)

Este é um projeto de um jogo da velha desenvolvido em Python, utilizando o algoritmo Minimax com poda alfa-beta para o modo jogador vs computador. O jogo conta com diferentes níveis de dificuldade e uma interface gráfica simples.

## Funcionalidades

- **Modos de Jogo**:
  - Jogador vs Jogador
  - Jogador vs Computador (com níveis de dificuldade)
  
- **Níveis de Dificuldade**:
  - **Fácil**: O computador faz movimentos aleatórios.
  - **Médio**: O computador usa o algoritmo Minimax com profundidade limitada a 2 jogadas.
  - **Difícil**: O computador usa o algoritmo Minimax completo com poda alfa-beta, sem limite de profundidade.
  
- **Interface Gráfica**: Simples e intuitiva, desenvolvida em Python.

## Algoritmo Minimax

O algoritmo Minimax é utilizado para determinar o movimento ideal do computador. Ele explora todas as possibilidades de jogadas, escolhendo a melhor com base em uma heurística que prioriza vencer e evitar perder.

### Poda Alfa-Beta

A poda alfa-beta é uma otimização aplicada ao Minimax que reduz o número de nós avaliados na árvore de decisão, melhorando a eficiência do algoritmo sem alterar o resultado final.

## Estrutura do Projeto

- `TicTacToe.py`: Gerencia o menu principal e a seleção de modos de jogo.
- `Game.py`: Controla a lógica do jogo da velha.
- `ComputerPlayer.py`: Implementa a lógica da IA, incluindo o algoritmo Minimax com poda alfa-beta.
- `Player.py`: Define os jogadores, sejam eles humanos ou a IA.

## Requisitos

- Python 3.10.11 ou superior
- Bibliotecas: Tkinter

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/MaykollRocha/JogoDaVelhaMinMax.git
   cd JogoDaVelhaMinMax
   ```
2. Entrar na Venv:
   ```bash
   .\MaxMinVenv\Scripts\Activate.ps1 
   ```
3. Execute o jogo:
   ```bash
   python main.py
   ```

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests!
