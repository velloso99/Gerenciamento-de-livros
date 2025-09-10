import sqlite3

#Conectar ao banco de dados e criar um novo banco de dados
con = sqlite3.connect('dados.db')


#Criar uma tabela de livros
con.execute('CREATE TABLE livros( \
                id INTEGER PRIMARY KEY, \
                titulo TEXT,\
                autor TEXT,\
                editora TEXT, \
                ano_publicacao INTEGER,\
                ISBN TEXT)')

#Criando tabela de usuarios
con.execute('CREATE TABLE usuarios( \
                id INTEGER PRIMARY KEY, \
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT, \
                email TEXT,\
                contato TEXT)')

#Criando tabela de emprestimo
con.execute('CREATE TABLE emprestimos(\
                id INTEGER PRIMARY KEY,\
                id_livro INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREIGN KEY (id_livro) REFERENCES livros(id),\)')


