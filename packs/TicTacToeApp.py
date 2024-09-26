import tkinter as tk

from PIL import Image, ImageTk  # type: ignore

from packs.ComputerPlayer import *
from packs.Game import *
from packs.GlobalVars import *


class TicTacToeApp:
    """
    Classe que representa o jogo da velha usando tkinter para a interface gráfica.

    Atributos:
        root (tk.Tk): A janela principal do aplicativo tkinter.
        menu_frame (tk.Frame): O frame que contém o menu principal do jogo.
        buttons (list): Lista de botões que representam o tabuleiro de jogo.
        computer_player (ComputerPlayer): Representa o jogador de computador no modo Humano vs Computador.
        computer_player_x (ComputerPlayer): IA representando o jogador X no modo IA vs IA.
        computer_player_o (ComputerPlayer): IA representando o jogador O no modo IA vs IA.
        current_player (str): Indica o jogador atual ('X' ou 'O').

    Métodos:
        __init__(self, root): Inicializa a interface do jogo e define configurações iniciais.
        create_menu(self): Cria o menu principal com as opções de jogo.
        start_human_vs_human(self): Inicia o jogo no modo Humano vs Humano.
        start_human_vs_computer(self, difficulty): Inicia o jogo no modo Humano vs Computador, com dificuldade variável.
        start_ai_vs_ai(self): Inicia o jogo no modo IA vs IA.
        setup_game(self): Configura o tabuleiro para um novo jogo.
        create_board(self): Cria o tabuleiro do jogo com botões interativos.
        on_button_click(self, index): Gerencia os cliques no tabuleiro e atualiza o estado do jogo.
        check_winner(self, player): Verifica se um jogador venceu ou se houve empate.
        disable_all_buttons(self): Desabilita todos os botões após o término do jogo.
        update_status(self, message, colorMsg): Atualiza a mensagem de status exibida na interface.
        back_to_menu(self): Retorna ao menu principal, destruindo o tabuleiro atual.
    """

    def __init__(self, root):
        """
        Inicializa a janela principal do jogo e define as configurações da interface.

        Args:
            root (tk.Tk): A janela principal da interface gráfica tkinter.
        """
        self.root = root
        self.root.title("Jogo da Velha")

        # Carrega o ícone da janela
        icon_path = "imgs/tic-tac-toe_39453.png"  # Substitua pelo caminho do ícone .png
        icon_image = Image.open(icon_path)
        icon_photo = ImageTk.PhotoImage(icon_image)
        root.iconphoto(False, icon_photo)

        # Impede o redimensionamento da janela.
        self.root.resizable(False, False)
         
        # Variável para armazenar o estado do modo debug
        self.debug_mode = tk.StringVar(value=False)  # Padrão: Off
        # Cria o menu principal do jogo.
        self.create_menu()

    def create_menu(self):
        """
        Cria o menu principal com as opções de jogo e configura os botões para iniciar diferentes modos de jogo.
        """
        self.menu_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        self.menu_frame.grid()

        tk.Label(self.menu_frame, text="Jogo da Velha", font=('Arial', 24), bg=BACKGROUND_COLOR).grid(row=0,column=0,columnspan=3,padx=5,pady=5)

        # Botão "Humano vs Humano"
        self.create_menu_button("Humano vs Humano", self.start_human_vs_human).grid(row=1,column=0,columnspan=3,padx=5,pady=5)
        
        # Seção "Humano vs Computador"
        tk.Label(self.menu_frame, text="Humano vs Computador", font=('Arial', 14), bg=BACKGROUND_COLOR).grid(row=2,column=0,columnspan=3,padx=5,pady=5)
        tk.Label(self.menu_frame, text="Selecione a Dificuldade:", font=('Arial', 14), bg=BACKGROUND_COLOR).grid(row=3,column=0,columnspan=3,padx=5,pady=5)
        
        # Botões de Dificuldade usando pack
        self.create_menu_button("Fácil", lambda: self.start_human_vs_computer(difficulty='easy')).grid(row=4,column=0,padx=2,pady=5)
        self.create_menu_button("Médio", lambda: self.start_human_vs_computer(difficulty='medium')).grid(row=4,column=1,padx=2,pady=5)
        self.create_menu_button("Difícil", lambda: self.start_human_vs_computer(difficulty='hard')).grid(row=4,column=2,padx=2,pady=5)
        tk.Label(self.menu_frame, text="Modo IA x IA com dificuldade\n Dificil nas Duas", font=('Arial', 14), bg=BACKGROUND_COLOR).grid(row=5,column=0,columnspan=3,padx=5,pady=5)
        # Botão "IA vs IA"
        self.create_menu_button("IA vs IA", self.start_ai_vs_ai).grid(row=6, column=0, columnspan=3, padx=5, pady=5)
        
        # Seção para modo debug
        tk.Label(self.menu_frame, text="Modo Debug:", font=('Arial', 14), bg=BACKGROUND_COLOR).grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        # Radio buttons para selecionar o modo debug
        tk.Radiobutton(self.menu_frame, text="Ativado", variable=self.debug_mode, value=True, bg=BACKGROUND_COLOR).grid(row=8, column=0, padx=5, pady=5)
        tk.Radiobutton(self.menu_frame, text="Desativado", variable=self.debug_mode, value=False, bg=BACKGROUND_COLOR).grid(row=8, column=2, padx=5, pady=5)

    def start_human_vs_human(self):
        """
        Inicia o jogo no modo Humano vs Humano, configurando o tabuleiro e definindo o jogador atual.
        """
        self.menu_frame.destroy()
        self.setup_game()
        self.current_player = 'X'
        self.human_vs_human()

    def human_vs_human(self):
        """
        Atualiza a interface com o status do jogo no modo Humano vs Humano.
        """
        self.update_status("Jogador X começa", BUTTON_COLOR_X)

    def start_human_vs_computer(self, difficulty='hard'):
        """
        Inicia o jogo no modo Humano vs Computador, configurando o tabuleiro, o jogador de computador e a dificuldade.

        Args:
            difficulty (str): A dificuldade do jogo para o computador ('easy', 'medium', 'hard').
        """
        self.menu_frame.destroy()
        self.setup_game()
        self.computer_player = ComputerPlayer('O', difficulty=difficulty)
        self.current_player = 'X'
        self.human_vs_computer()

    def human_vs_computer(self):
        """
        Atualiza a interface com o status do jogo no modo Humano vs Computador.
        """
        self.update_status("Jogador X começa", BUTTON_COLOR_X)

    def computer_move(self):
        """
        Realiza a jogada do computador e atualiza o estado do jogo. Se o computador vencer, a função termina.
        """
        if hasattr(self, 'computer_player') and self.computer_player:
            move = self.computer_player.get_move(self.game)
            self.buttons[move].config(text='O', fg=BUTTON_COLOR_O)
            self.game.make_move(move, 'O')
            if self.check_winner('O'):
                return
            self.current_player = 'X'
            self.update_status("Vez do jogador X", BUTTON_COLOR_X)
        else:
            self.update_status("Erro: Jogador Computador não inicializado", "#FF0000")

    def start_ai_vs_ai(self):
        """
        Inicia o jogo no modo IA vs IA, configurando o tabuleiro e as IAs dos jogadores.
        """
        self.menu_frame.destroy()
        self.setup_game()
        self.computer_player_x = ComputerPlayer('X')
        self.computer_player_o = ComputerPlayer('O',)
        self.current_player = 'X'
        self.ai_vs_ai()

    def ai_vs_ai(self):
        """
        Atualiza a interface com o status do jogo no modo IA vs IA e inicia o movimento da IA.
        """
        self.update_status("IA X começa", BUTTON_COLOR_X)
        self.root.after(500, self.ai_move)

    def ai_move(self):
        """
        Realiza a jogada da IA e alterna entre as IAs X e O. O próximo movimento é agendado após 500 ms.
        """
        if self.game.empty_squares():
            if self.current_player == 'X':
                move = self.computer_player_x.get_move(self.game)
                self.buttons[move].config(text='X', fg=BUTTON_COLOR_X)
                self.game.make_move(move, 'X')
                if self.check_winner('X'):
                    return
                self.current_player = 'O'
                self.root.after(500, self.ai_move)
            else:
                move = self.computer_player_o.get_move(self.game)
                self.buttons[move].config(text='O', fg=BUTTON_COLOR_O)
                self.game.make_move(move, 'O')
                if self.check_winner('O'):
                    return
                self.current_player = 'X'
                self.root.after(500, self.ai_move)

    def setup_game(self):
        """
        Configura o tabuleiro para um novo jogo e inicializa os componentes da interface gráfica.
        """
        if hasattr(self, 'board_frame'):
            self.board_frame.destroy()
        if hasattr(self, 'status_label'):
            self.status_label.destroy()
        if hasattr(self, 'back_to_menu_button'):
            self.back_to_menu_button.pack_forget()

        self.game = Game(self.debug_mode.get())
        self.create_board()

    def create_menu_button(self, text, command):
        """
        Cria um botão de menu com o texto especificado e o comando associado.

        Args:
            text (str): O texto a ser exibido no botão.
            command (callable): A função a ser chamada quando o botão for clicado.

        Returns:
            tk.Button: O botão de menu configurado.
        """
        button = tk.Button(self.menu_frame, text=text, font=MENU_BUTTON_FONT, bg=MENU_BUTTON_COLOR, 
                           activebackground=MENU_BUTTON_HOVER_COLOR, command=command)
        button.bind("<Enter>", self.on_hover)
        button.bind("<Leave>", self.on_leave)
        return button

    def on_hover(self, event):
        """
        Altera a cor de fundo do botão quando o cursor está sobre ele.

        Args:
            event (tk.Event): O evento de sobreposição do cursor.
        """
        event.widget.config(bg=MENU_BUTTON_HOVER_COLOR)

    def on_leave(self, event):
        """
        Restaura a cor de fundo do botão quando o cursor sai dele.

        Args:
            event (tk.Event): O evento de saída do cursor.
        """
        event.widget.config(bg=MENU_BUTTON_COLOR)

    def create_board(self):
        """
        Cria o tabuleiro do jogo com botões interativos e a área de status.
        """
        self.buttons = []
        self.root['bg'] = BACKGROUND_COLOR
        self.board_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR_BOARD)
        self.board_frame.pack()

        for i in range(9):
            button = tk.Button(self.board_frame, text='', font=BUTTON_FONT, width=5, height=2,
                               bg=BUTTON_COLOR_DEFAULT, command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3, padx=2, pady=2)
            self.buttons.append(button)

        self.status_label = tk.Label(self.root, text='', font=STATUS_FONT, bg=BACKGROUND_COLOR, fg=STATUS_COLOR)
        self.status_label.pack(pady=10)

        self.back_to_menu_button = tk.Button(self.root, text="Voltar ao Menu", font=STATUS_FONT, bg=MENU_BUTTON_COLOR, 
                           activebackground=MENU_BUTTON_HOVER_COLOR, command=self.back_to_menu)
        self.back_to_menu_button.bind("<Enter>", self.on_hover)
        self.back_to_menu_button.bind("<Leave>", self.on_leave)
        self.back_to_menu_button.pack(pady=10)

    def on_button_click(self, index):
        """
        Gerencia o clique em um botão do tabuleiro e atualiza o estado do jogo.

        Args:
            index (int): O índice do botão clicado.
        """
        if self.game.board[index] == ' ' and self.current_player in ['X', 'O']:
            if self.current_player == 'X':
                self.buttons[index].config(text='X', fg=BUTTON_COLOR_X)
                self.game.make_move(index, 'X')
                if self.check_winner('X'):
                    return
                self.current_player = 'O'
                if hasattr(self, 'computer_player') and self.computer_player:
                    self.root.after(500, self.computer_move)
            else:
                self.buttons[index].config(text='O', fg=BUTTON_COLOR_O)
                self.game.make_move(index, 'O')
                if self.check_winner('O'):
                    return
                self.current_player = 'X'
            self.update_status(f"Vez do jogador {self.current_player}", BUTTON_COLOR_X if self.current_player == 'X' else BUTTON_COLOR_O)

    def check_winner(self, player):
        """
        Verifica se um jogador venceu ou se houve empate e atualiza a interface com a mensagem correspondente.

        Args:
            player (str): O jogador ('X' ou 'O') a ser verificado.

        Returns:
            bool: Retorna True se houve uma vitória ou empate, False caso contrário.
        """
        if self.game.current_winner:
            self.update_status(f"Jogador {player} venceu!", "#00FF00")
            self.disable_all_buttons()
            return True
        if not self.game.empty_squares():
            self.update_status("Empate!", "#000000")
            self.disable_all_buttons()
            return True
        return False

    def disable_all_buttons(self):
        """
        Desabilita todos os botões do tabuleiro após o término do jogo.
        """
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def update_status(self, message, colorMsg):
        """
        Atualiza a mensagem de status exibida na interface com a cor especificada.

        Args:
            message (str): A mensagem de status a ser exibida.
            colorMsg (str): A cor do texto da mensagem de status.
        """
        self.status_label.config(text=message, fg=colorMsg)

    def back_to_menu(self):
        """
        Retorna ao menu principal, destruindo o tabuleiro atual e os componentes associados.
        """
        self.board_frame.destroy()
        self.status_label.destroy()
        self.back_to_menu_button.pack_forget()
        self.computer_player = None
        self.computer_player_x = None
        self.computer_player_o = None
        self.create_menu()
