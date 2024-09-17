class Player:
    def __init__(self, letter):
        """
        Inicializa o jogador com uma letra (X ou O).
        
        Args:
            letter (str): A letra do jogador ('X' ou 'O').
        """
        self.letter = letter

    def get_move(self, game):
        """
        Método abstrato para obter o movimento do jogador. Deve ser implementado pelas subclasses.
        
        Args:
            game (Game): A instância do jogo em que o movimento será feito.
        
        Returns:
            int: O índice do espaço onde o jogador deseja fazer a jogada.
        """
        pass
