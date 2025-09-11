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
################################################################################################
#novo Usuario
def novo_usuario():

    global img_salvar

    app_titulo =Label(frame_direita, text="Inserir um novo usuario", width=50, compound=LEFT, padx=5, pady=10, font=("Verdana 12 bold"), bg=co1, fg=co4 )
    app_titulo.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_linha= Label(frame_direita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    l_p_nome =Label(frame_direita, text="Primeiro Nome*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_p_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_nome =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_p_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_sobrenome =Label(frame_direita, text="Sobrenome*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_sobrenome =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_endereco =Label(frame_direita, text="Endereço do usuario*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_endereco =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_email =Label(frame_direita, text="Endereco do E-mail*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_email =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_contato =Label(frame_direita, text="Contato*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_contato.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_contato =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_contato.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    img_salvar = Image.open('img/save.png')
    img_salvar = img_salvar .resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar )
    b_salvar =Button(frame_direita, image=img_salvar, compound=LEFT, width=100 ,anchor=NW, text=' Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, sticky=NSEW, pady=6)



################################################################################################
# Configuração
#Função para controlar o menu
def control(i):
    #novo usuario
    if i == 'novo usuario':
        for windget in frame_direita.winfo_children():
            windget.destroy()
        # Chamando a função novo usuario
        novo_usuario()










#################################################################################################
# Logo 
# Abrir imagem
app_img = Image.open('img/logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo= Label(frame_cima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW,bg=co6, fg=co1)
app_logo.place(x=5, y=0)
app_= Label(frame_cima, text="Sistema de Gerencimento de Livros",compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'),bg=co6, fg=co1)
app_.place(x=50, y=7)

app_linha= Label(frame_cima,width=770, height=1, padx=5, anchor=NW, font=('Verdana 1'),bg=co3, fg=co1)
app_linha.place(x=0, y=47)

#########################################################################################################
# Menu
# Abrir imagem novo usuario
img_usuario = Image.open('img/add.png')
img_usuario = img_usuario .resize((18,18))
img_usuario = ImageTk.PhotoImage(img_usuario )
b_usuario =Button(frame_esquerda,command=lambda:control('novo usuario') ,image=img_usuario, compound=LEFT, anchor=NW, text=' Novo Usuario', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Abrir imagem novo livro
img_livro = Image.open('img/add.png')
img_livro = img_livro .resize((18,18))
img_livro = ImageTk.PhotoImage(img_livro )
b_livro =Button(frame_esquerda, image=img_livro, compound=LEFT, anchor=NW, text=' Novo Livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Abrir imagem ver livros
img_ver_livro = Image.open('img/logo.png')
img_ver_livro = img_ver_livro .resize((18,18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro )
b_ver_livro =Button(frame_esquerda, image=img_ver_livro, compound=LEFT, anchor=NW, text=' Exibir todo os livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Abrir imagem ver Usuarios
img_ver_usuarios = Image.open('img/user.png')
img_ver_usuarios = img_ver_usuarios .resize((18,18))
img_ver_usuarios = ImageTk.PhotoImage(img_ver_usuarios )
b_ver_usuarios =Button(frame_esquerda, image=img_ver_usuarios, compound=LEFT, anchor=NW, text=' Exibir todos os Usuarios', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuarios.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Abrir imagem Realizar um emprestimo
img_emprestimos = Image.open('img/add.png')
img_emprestimos = img_emprestimos .resize((18,18))
img_emprestimos = ImageTk.PhotoImage(img_emprestimos )
b_emprestimos = Button(frame_esquerda, image=img_emprestimos, compound=LEFT, anchor=NW, text=' Realizar emprestimos', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestimos.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Abrir imagem devolução de  um emprestimo
img_devolucao_emprestimos = Image.open('img/update.png')
img_devolucao_emprestimos = img_devolucao_emprestimos .resize((18,18))
img_devolucao_emprestimos = ImageTk.PhotoImage(img_devolucao_emprestimos )
b_devolucao_emprestimos = Button(frame_esquerda, image=img_devolucao_emprestimos, compound=LEFT, anchor=NW, text=' Devolução de livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_devolucao_emprestimos.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Abrir imagem livros emprestados
img_livros_emprestados = Image.open('img/book.png')
img_livros_emprestados = img_livros_emprestados .resize((18,18))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados )
b_livros_emprestados = Button(frame_esquerda, image=img_livros_emprestados, compound=LEFT, anchor=NW, text=' Livros emprestado no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)
#########################################################################################################################################################################################################################

















janela.mainloop()



