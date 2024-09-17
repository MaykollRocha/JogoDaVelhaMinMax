class Game:
    def __init__(self, state):
        """
        Inicializa o tabuleiro com 9 espaços vazios e define o estado de depuração.

        Args:
            state (str): Define se o modo de depuração está ativado ('1' para True, qualquer outra coisa para False).
        """
        self.board = [' ' for _ in range(9)]  # Tabuleiro 3x3
        self.current_winner = None  # Monitorar o vencedor
        self.debug_mode = True if state == '1' else False

    def print_board(self):
        """
        Imprime o estado atual do tabuleiro no console. O tabuleiro é impresso em formato 3x3.
        """
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        """
        Retorna uma lista de índices dos espaços disponíveis no tabuleiro.

        Returns:
            list: Lista de índices dos espaços vazios.
        """
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        """
        Verifica se há espaços vazios no tabuleiro.

        Returns:
            bool: True se houver espaços vazios, False caso contrário.
        """
        return ' ' in self.board

    def num_empty_squares(self):
        """
        Conta o número de espaços vazios no tabuleiro.

        Returns:
            int: O número de espaços vazios.
        """
        return self.board.count(' ')

    def make_move(self, square, letter):
        """
        Faz uma jogada no tabuleiro se o espaço especificado estiver vazio. Atualiza o vencedor atual se a jogada resultar em vitória.

        Args:
            square (int): O índice do espaço onde a jogada será feita.
            letter (str): A letra do jogador ('X' ou 'O') que fará a jogada.

        Returns:
            bool: True se a jogada foi bem-sucedida, False se o espaço já estiver ocupado.
        """
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """
        Verifica se a jogada feita resultou em uma vitória para o jogador com a letra fornecida.

        Args:
            square (int): O índice do espaço onde a jogada foi feita.
            letter (str): A letra do jogador ('X' ou 'O') que fez a jogada.

        Returns:
            bool: True se a jogada resultou em vitória, False caso contrário.
        """
        # Verifica a linha onde o espaço está localizado
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Verifica a coluna onde o espaço está localizado
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Verifica as diagonais, se o espaço estiver em uma posição de diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False
