from tkinter import ttk
from tkinter .ttk import*
from  tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

#Importando as funções da Viewa
from view import *

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

    def add():

        first_name = e_p_nome.get()
        last_name = e_sobrenome.get()
        andress = e_endereco.get()
        email = e_email.get()
        phone = e_contato.get()

        lista =[first_name,last_name,andress,email,phone]

        #Verificando caso algum campo esteja vazio ou não
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', "Preencha todos os campos")
                return

        #inserindo os dados no banco de dados 
        insert_user(first_name,last_name,andress,email,phone)

        messagebox.showinfo('Sucesso', 'Usuario inserido com sucesso')

        #limpando os campos de entrada
        e_p_nome.delete(0,END)
        e_sobrenome.delete(0,END)
        e_endereco.delete(0,END)
        e_email.delete(0,END)
        e_contato.delete(0,END)

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
    b_salvar = Button(frame_direita,command=add ,image=img_salvar, compound=LEFT, width=100 ,anchor=NW, text=' Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, sticky=NSEW, pady=6)
#####################################################################################################################
#Ver Usuario
def ver_usuarios():

        app_ = Label(frame_direita,text="Todos os usuários do banco de dados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12 bold'),bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frame_direita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = get_user()

        #creating a treeview with dual scrollbars
        list_header = ['ID','Nome','Sobrenome','Endereço','Email','Contato']
    
        global tree

        tree = ttk.Treeview(frame_direita, selectmode="extended", columns=list_header, show="headings")
        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frame_direita.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","nw","nw","nw"]
        h=[20,80,80,120,120,76,100]
        n=0

        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            #adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
        
            n+=1

        for item in dados:
            tree.insert('', 'end', values=item)

##################################################################################################################
def novos_livros():

    global img_salvar

    def add():

        title_book = e_titulo_livro.get()
        author_book = e_autor_livro.get()
        editor_book = e_editora_livro.get()
        publication = e_Publicacao.get()
        isbn = e_ISBN.get()

        lista =[title_book,author_book ,editor_book,publication,isbn]

        #Verificando caso algum campo esteja vazio ou não
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', "Preencha todos os campos")
                return

        #inserindo os dados no banco de dados 
        insert_book(title_book,author_book ,editor_book,publication,isbn)

        messagebox.showinfo('Sucesso', 'Usuario inserido com sucesso')

        #limpando os campos de entrada
        e_titulo_livro.delete(0,END)
        e_autor_livro.delete(0,END)
        e_editora_livro.delete(0,END)
        e_Publicacao.delete(0,END)
        e_ISBN.delete(0,END)

    app_titulo =Label(frame_direita, text="Inserir um novo livros", width=50, compound=LEFT, padx=5, pady=10, font=("Verdana 12 bold"), bg=co1, fg=co4 )
    app_titulo.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha= Label(frame_direita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    l_titulo_livro =Label(frame_direita, text="Titulo do Livro*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_titulo_livro.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_titulo_livro =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_titulo_livro.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_autor_livro =Label(frame_direita, text="Autor do Livro*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_autor_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor_livro =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_autor_livro.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_editora_livro =Label(frame_direita, text="Editora do Livro*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_editora_livro.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora_livro =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_editora_livro.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_Publicacao =Label(frame_direita, text="Ano de publicação do livro*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_Publicacao.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_Publicacao =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_Publicacao.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_ISBN =Label(frame_direita, text="ISBN do livro*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_ISBN.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_ISBN =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_ISBN.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    img_salvar = Image.open('img/save.png')
    img_salvar = img_salvar .resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar )
    b_salvar = Button(frame_direita,command=add ,image=img_salvar, compound=LEFT, width=100 ,anchor=NW, text=' Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, sticky=NSEW, pady=6)

##########################################################################################################################
#Ver Usuario
def ver_livros():

        app_ = Label(frame_direita,text="Todos os livros no banco de dados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12 bold'),bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frame_direita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = exibir_livros()

        #creating a treeview with dual scrollbars
        list_header = ['ID','Livro','Autor','Editora','Ano Publicação','ISBN']
    
        global tree

        tree = ttk.Treeview(frame_direita, selectmode="extended", columns=list_header, show="headings")
        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frame_direita.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","nw","nw","nw"]
        h=[20,165,110,120,50,50,100]
        n=0

        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            #adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
        
            n+=1

        for item in dados:
            tree.insert('', 'end', values=item)

###############################################################################################################
# Realizar emprestimos
def realizar_emprestimo():

    global img_salvar

    def add():


        id_user= e_id_usario.get()
        id_book = e_id_livro.get()
        
        
        lista =[id_book, id_user]

        #Verificando caso algum campo esteja vazio ou não
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', "Preencha todos os campos")
                return

        #inserindo os dados no banco de dados 
        insert_loan(id_book, id_user, None, None)

        messagebox.showinfo('Sucesso', 'Emprestimo inserido com sucesso')

        #limpando os campos de entrada
        e_id_usario.delete(0,END)
        e_id_livro.delete(0,END)
       

    app_titulo =Label(frame_direita, text="Realizar um  Emprestimo", width=50, compound=LEFT, padx=5, pady=10, font=("Verdana 12 bold"), bg=co1, fg=co4 )
    app_titulo.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha= Label(frame_direita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    l_id_usario =Label(frame_direita, text="Digite o ID do usuario*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_id_usario.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_usario =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_id_usario.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_id_livro =Label(frame_direita, text="Digite o ID do livro*", anchor=NW ,font=("Ivy 10"), bg=co1, fg=co4 )
    l_id_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_livro =Entry(frame_direita, width=25, justify='left', relief='solid')
    e_id_livro.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    img_salvar = Image.open('img/save.png')
    img_salvar = img_salvar .resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar )
    b_salvar = Button(frame_direita,command=add ,image=img_salvar, compound=LEFT, width=100 ,anchor=NW, text=' Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, sticky=NSEW, pady=6)

####################################################################################################################
#Ver livros Emprestados 
def ver_livros_emprestados():

        app_ = Label(frame_direita,text="Todos os livros Emprestados no momento",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12 bold'),bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frame_direita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = []
        books_on_loan = get_books_on_loan()
        for book in  books_on_loan:
            dado = [f"{book[0]}", f"{book[1]}", f"{book[2]} {book[3]}", f"{book[4]}", f"{book[5]}" ]

            dados.append(dado)

        #creating a treeview with dual scrollbars
        list_header = ['ID','Titulo','Nome Usuario','Data Emprestimo','Data Devolução']
    
        global tree

        tree = ttk.Treeview(frame_direita, selectmode="extended", columns=list_header, show="headings")
        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frame_direita.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","ne","ne","ne","ne"]
        h=[20,175,120,90,90,100,100]
        n=0

        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            #adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
        
            n+=1

        for item in dados:
            tree.insert('', 'end', values=item)






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

    #Ver usuario
    if i == 'ver usuarios':
        for windget in frame_direita.winfo_children():
            windget.destroy()
        # Chamando a função novo usuario
        ver_usuarios()

    #novos livros
    if i == 'novos livros':
        for windget in frame_direita.winfo_children():
            windget.destroy()
        # Chamando a função novo usuario
        novos_livros()

    #Ver usuario
    if i == 'ver livros':
        for windget in frame_direita.winfo_children():
            windget.destroy()
        # Chamando a função ver livros
        ver_livros()

    #emprestimo de livros
    if i == 'emprestimo livros':
        for windget in frame_direita.winfo_children():
            windget.destroy()
        # Chamando a função emprestimo de livros
        realizar_emprestimo()

    # Ver Livros Emprestados
    if i == 'ver livros emprestados':
        for windget in frame_direita.winfo_children():
            windget.destroy()
        # Chamando a função ver livros emprstados
        ver_livros_emprestados()



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
b_livro =Button(frame_esquerda,command=lambda:control('novos livros'), image=img_livro, compound=LEFT, anchor=NW, text=' Novo Livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Abrir imagem ver livros
img_ver_livro = Image.open('img/logo.png')
img_ver_livro = img_ver_livro .resize((18,18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro )
b_ver_livro =Button(frame_esquerda,command=lambda:control('ver livros') ,image=img_ver_livro, compound=LEFT, anchor=NW, text=' Exibir todo os livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Abrir imagem ver Usuarios
img_ver_usuarios = Image.open('img/user.png')
img_ver_usuarios = img_ver_usuarios .resize((18,18))
img_ver_usuarios = ImageTk.PhotoImage(img_ver_usuarios )
b_ver_usuarios =Button(frame_esquerda, command=lambda:control('ver usuarios')  ,image=img_ver_usuarios, compound=LEFT, anchor=NW, text=' Exibir todos os Usuarios', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuarios.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Abrir imagem Realizar um emprestimo
img_emprestimos = Image.open('img/add.png')
img_emprestimos = img_emprestimos .resize((18,18))
img_emprestimos = ImageTk.PhotoImage(img_emprestimos )
b_emprestimos = Button(frame_esquerda,command=lambda:control('emprestimo livros') ,image=img_emprestimos, compound=LEFT, anchor=NW, text=' Realizar emprestimos', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
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
b_livros_emprestados = Button(frame_esquerda, command=lambda:control('ver livros emprestados') , image=img_livros_emprestados, compound=LEFT, anchor=NW, text=' Livros emprestado no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)
#########################################################################################################################################################################################################################

















janela.mainloop()



