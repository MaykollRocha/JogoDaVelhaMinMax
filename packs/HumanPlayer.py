from packs.Player import *


class HumanPlayer(Player):
    def __init__(self, letter):
        """
        Inicializa o jogador humano com uma letra (X ou O). Herda da classe base Player.
        
        Args:
            letter (str): A letra do jogador ('X' ou 'O').
        """
        super().__init__(letter)

    def get_move(self, game):
        """
        Obtém o movimento do jogador humano. Solicita ao usuário para inserir um movimento válido e retorna o índice do movimento.
        
        Args:
            game (Game): A instância do jogo em que o movimento será feito.
        
        Returns:
            int: O índice do espaço onde o jogador deseja fazer a jogada.
        """
        valid_square = False
        val = None
        while not valid_square:
            # Solicita ao jogador humano que insira um movimento
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                # Converte a entrada do usuário para um inteiro
                val = int(square)
                # Verifica se o movimento está disponível
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                # Exibe uma mensagem de erro se a entrada não for válida
                print('Invalid square. Try again.')
        return val

