import math
import random
import secrets  # Para gerar números aleatórios usados em criptografia.

from packs.Player import *


class ComputerPlayer(Player):
    def __init__(self, letter, difficulty='hard'):
        """
        Inicializa o jogador computador com uma letra (X ou O) e um nível de dificuldade.

        Args:
            letter (str): A letra do jogador ('X' ou 'O').
            difficulty (str): Nível de dificuldade ('easy', 'medium', 'hard').
        """
        super().__init__(letter)
        self.difficulty = difficulty

    def get_move(self, game):
        """
        Obtém o movimento do jogador computador baseado no nível de dificuldade.

        Args:
            game (Game): A instância do jogo em que o movimento será feito.

        Returns:
            int: O índice do espaço onde o computador deseja fazer a jogada.
        """
        if len(game.available_moves()) == 9:
            square = secrets.randbelow(9)
        elif self.difficulty == 'easy':
            square = random.choice(game.available_moves()) if game.available_moves() else None    
        elif self.difficulty == 'medium':
            square = self.minimax(game, self.letter, depth=2)['position']
        elif self.difficulty == 'hard':  # Hard
            square = self.minimax(game, self.letter)['position']
        
        if game.debug_mode:
            print('\n-----------------------------------------')
        return square
    
    def heuristic_state(self, state):
        """
        Avalia o estado do tabuleiro com base na heurística para determinar a qualidade de uma jogada.

        Args:
            state (Game): O estado atual do jogo.

        Returns:
            int: Pontuação heurística do estado.
        """
        win_cases = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        
        if state.current_winner == self.letter:  # Vitória da IA
            if state.debug_mode:
                state.print_board()
                print(f"Vencedor: {state.current_winner}, Score: {1 * (state.num_empty_squares() + 1)}")
            return 1 * (state.num_empty_squares() + 1)
        elif state.current_winner == ('O' if self.letter == 'X' else 'X'):  # Vitória do adversário
            if state.debug_mode:
                state.print_board()
                print(f"Vencedor: {state.current_winner}, Score: {-1 * (state.num_empty_squares() + 1)}")
            return -1 * (state.num_empty_squares() + 1)
        else:
            score = 0
            for (i, j, k) in win_cases:
                line = [state.board[i], state.board[j], state.board[k]]
                if line.count(self.letter) == 2 and line.count(' ') == 1:
                    score += 5  # Jogada próxima de vitória
                elif line.count(('O' if self.letter == 'X' else 'X')) == 2 and line.count(' ') == 1:
                    score -= 5  # Jogada que precisa ser bloqueada
            
            if state.debug_mode:
                state.print_board()
                print(f"Possível futura boa jogada: {score}")
            
            return score
    
    def minimax(self, state, player, depth=math.inf, alpha=-math.inf, beta=math.inf):
        """
        Implementa o algoritmo Minimax com poda alfa-beta para determinar o melhor movimento para o computador.

        Args:
            state (Game): O estado atual do jogo.
            player (str): O jogador atual ('X' ou 'O').
            depth (int, opcional): Profundidade máxima da árvore de decisão. Default é infinito.
            alpha (float, opcional): Valor alpha para poda alfa-beta. Default é -infinito.
            beta (float, opcional): Valor beta para poda alfa-beta. Default é infinito.

        Returns:
            dict: Um dicionário contendo a 'position' do melhor movimento e a 'score' correspondente.
        """
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # Caso base: verifica se houve um vencedor ou se o jogo está terminado
        if state.current_winner or not state.empty_squares() or depth == 0:
            return {'position': None, 'score': self.heuristic_state(state)}

        # Inicializa o melhor movimento
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        moves = state.available_moves()
        
        for possible_move in moves:
            # Faz o movimento
            state.make_move(possible_move, player)
            
            # Simula o jogo para o jogador adversário
            sim_score = self.minimax(state, other_player, depth - 1, alpha, beta)

            # Desfaz o movimento
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                alpha = max(alpha, best['score'])
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, best['score'])
                

            # Poda alfa-beta
            if beta <= alpha:
                if state.debug_mode:
                    print(f"Poda: alpha={alpha}, beta={beta}, cortando ramos")  
                break
        #Retorna o melhor valor, para o estado ou para a jogada.
        return best

