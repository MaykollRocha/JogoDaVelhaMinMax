import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas.

# Importa a classe TicTacToeApp do módulo 'TicTacToeApp' dentro do pacote 'packs'.
from packs.TicTacToeApp import *

if __name__ == "__main__":
    """
    Função principal que configura e inicia a aplicação de jogo da velha.

    Cria a janela principal da aplicação e instancia a classe TicTacToeApp,
    que gerencia a lógica e a interface do jogo da velha. Em seguida, inicia
    o loop principal da aplicação para manter a janela aberta e processar eventos.
    """
    # Cria a janela principal da aplicação.
    root = tk.Tk()
    
    # Instancia a classe TicTacToeApp, passando a janela principal 'root' como parâmetro.
    app = TicTacToeApp(root)
    
    # Inicia o loop principal da aplicação, que mantém a janela aberta
    # e processa eventos, como cliques de botão.
    root.mainloop()
