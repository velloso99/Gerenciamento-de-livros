import sqlite3

#Conectar ao banco de dados e criar um novo banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Função para inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao ,isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao ,isbn) values(?,?,?,?,?)", (titulo, autor, editora, ano_publicacao ,isbn))
    conn.commit()
    conn.close()

# Função para inserir novo usuarios
def insert_user(nome, sobrenome, endereco, email, contato):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, contato) values(?,?,?,?,?)", (nome, sobrenome, endereco, email, contato))
    conn.commit()
    conn.close()

# Função para exibir os livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()

    if not livros:
        print("Nenhum livro encontrado na biblioteca")
        return
    print("livros na biblioteca")
    for livro in livros:
        print(f"id: {livro[0]}")
        print(f"titulo: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"editora: {livro[3]}")
        print(f"ano de Publicação: {livro[4]}")
        print(f"ISBN: {livro[5]}")
        print("\n")

# Função para realizar eprestimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livros, id_usuarios, data_emprestimo, data_devolucao) values(?,?,?,?)" ,(id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Função exibiro todos os livreos emprestados
def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao\
                            FROM livros\
                            INNER JOIN emprestimos ON livros.id = emprestimos.id_livros\
                            INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuarios\
                            WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

# Função para atualizar a data de devolução
def upload_loang_return_date(id_emprestimo, data_devolucao):
    conn =connect()
    conn.execute("UPDATE emprestimos SET data_devolucao =? WHERE id=?",(id_emprestimo, data_devolucao))
    conn.commit()
    conn.close()





