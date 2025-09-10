from tkinter .ttk import*
from  tkinter import *

from colors import *


###########################################################################################
# Crando Janela
janela = Tk()
janela.title("Gerenciamento de Livros")
janela.geometry('770x330')
janela.configure(background=co1)
janela.resizable(width=False, height=False)
#root.overrideredirect(1)
largura_root = 770
altura_root = 330
#obter tamanho da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
janela.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

Style = Style(janela)
Style.theme_use("clam")

#############################################################################################
# Frames

frame_cima= Frame(janela, width=770, height=50, bg=co6, relief="flat")
frame_cima.grid(row=0 , column=0, columnspan=2, sticky=NSEW)





janela.mainloop()



