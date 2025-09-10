from tkinter .ttk import*
from  tkinter import *
from PIL import Image, ImageTk

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
frame_cima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frame_esquerda= Frame(janela, width=150, height=265, bg=co4, relief="solid")
frame_esquerda.grid(row=1, column=0,sticky=NSEW)

frame_direita= Frame(janela, width=600, height=265, bg=co1, relief="raised")
frame_direita.grid(row=1, column=1, sticky=NSEW)

#################################################################################################
# Logo 
# Abrir imagem
app_img = Image.open('img/logo 2.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo= Label(frame_cima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW,bg=co6, fg=co1)
app_logo.place(x=5, y=0)
app_= Label(frame_cima, text="Sistema de Gerencimento de Livros",compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'),bg=co6, fg=co1)
app_.place(x=50, y=7)












janela.mainloop()



