import mysql.connector
from mysql.connector import errorcode

def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='root', database='ex1bd')
        print('Conexão realizada com BD', "Usuario:",conn.user,"Banco de dados:", conn.database)
        print(conn)
        return conn

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("BD não existe!")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario ou password errados!")
        else:
            print(error)

def desconectar(conn):
    """
    Função para desconectar do servidor.
    """
    if conn:
        conn.close();



def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor();
    cursor.execute('SELECT *FROM produtos');
    produtos = cursor.fetchall()
    if len(produtos) > 0:
        print("-------------LISTANDO PRODUTOS--------------")
        for produto in produtos:
            print(f'ID={produto[0]} DISCRIMINAÇÃO={produto[1]} PREÇO UNITÁRIO={produto[2]}')
        print("------------------")
    else:
        print("----------------- NÃO EXISTEM PRODUTOS NA LISTA --------------")
    desconectar(conn)
def inserir():
    """
    Função para inserir um produto
    """
    conn = conectar()
    cursor = conn.cursor();
    discriminacao = input("Informe a discriminação do produto: ")
    preco = float(input("Informe o preço do produto: "))

    cursor.execute(f"INSERT INTO produtos (discriminacao,p_unitario) VALUE ('{discriminacao}','{preco}')")
    conn.commit()
    if cursor.rowcount == 1 :
        print(f"O produto {discriminacao} foi inserido corretamente")
    else:
        print("Não foi possivel cadastrar o produto")
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()


    id = int(input("Informe o ID do produto que deseja atualizar: "))

    cursor.execute(f"SELECT * FROM produtos WHERE id = {id}")
    produto = cursor.fetchone()

    if produto:
        nova_discriminacao = input("Nova discriminação do produto: ")
        novo_preco = float(input("Novo preço do produto: "))

        cursor.execute(
            f"UPDATE produtos SET discriminacao = '{nova_discriminacao}', p_unitario = {novo_preco} WHERE id = {id}")
        conn.commit()

        if cursor.rowcount == 1:
            print(f"O produto com ID {id} foi atualizado corretamente.")
        else:
            print("Não foi possível atualizar o produto.")
    else:
        print(f"Produto com ID {id} não encontrado.")

    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    id = int(input("Informe o ID do produto que deseja deletar: "))

    cursor.execute(f"SELECT * FROM produtos WHERE id = {id}")
    produto = cursor.fetchone()

    if produto:
        cursor.execute(f"DELETE FROM produtos WHERE id = {id}")
        conn.commit()

        if cursor.rowcount == 1:
            print(f"O produto com ID {id} foi deletado corretamente.")
        else:
            print("Não foi possível deletar o produto.")
    else:
        print(f"Produto com ID {id} não encontrado.")

    desconectar(conn)


def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input("Selecione a opção desejada:"))
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')

