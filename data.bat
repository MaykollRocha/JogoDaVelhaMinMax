{
  "nome": "Jogo da Velha poda AlphaBeta - Trabalho IA",
  "infos": {
    "atividade": "Jogo da Velha algoritmo MaxMin com poda AlphaBeta",
    "dia": "Setembro de 2024"
  },
  "descrição": "Projeto desenvolvido na matéria de Inteligencia Artificial onde devo aplicar o algoritmo MaxMin com poda AlphaBeta",
  "Código": '''
            def heuristic_state(self, state):
        """
        Avalia o estado do tabuleiro com base na heurística para determinar a qualidade de uma jogada.

        Args:
            state (Game): O estado atual do jogo.

        Returns:
            int: Pontuação heurística do estado.
        """
        
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
            for (i, j, k) in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
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
            ''',
  "imag": None,
  "agregamento": "O seu tempo foi muito desafiador mas ao inciar começei a perceber a facilidade e a praticidade de fazer o codigo com a junção de anos de conhecimento meu codigo fico quase que impecavel ao se ver tem um documento no git explicando melhor como ele funciona e sua qualidae.",
  "link": "https://github.com/MaykollRocha/JogoDaVelhaMinMax"
}
