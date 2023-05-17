import mysql.connector

# Conectando ao banco de dados
config = {
  'user': 'admin',
  'password': 'aulanoiteFaculdade',
  'host': 'dbaula.cka0to8kgrtd.us-east-1.rds.amazonaws.com',
  'database': 'tribosBrazil'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

conn.close()


def inserir_tribo():
    nome = input("Nome da tribo: ")
    habitantes = int(input("Número de habitantes: "))
    renda_media = float(input("Renda média mensal: "))
    escolaridade = input("Escolaridade (fundamental, médio ou superior): ")
    trabalho_assalariado = input("Possui trabalho assalariado (sim ou não): ")

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        sql = """
            INSERT INTO tribos (nome_tribo, num_habitantes, renda_media, escolaridade, trabalho_assalariado)
            VALUES (%s, %s, %s, %s, %s)
        """
        data = (nome, habitantes, renda_media, escolaridade, trabalho_assalariado)
        cursor.execute(sql, data)
        conn.commit()
        print("Tribo cadastrada com sucesso!")
    except mysql.connector.Error as err:
        print("Erro ao inserir a tribo: {}".format(err))
    finally:
        cursor.close()
        conn.close()

# Função para listar todas as tribos cadastradas
def listar_tribos():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tribos")
        tribos = cursor.fetchall()
        if not tribos:
            print("Nenhuma tribo encontrada.")
        else:
            for tribo in tribos:
                print("ID: {}, Nome: {}, Habitantes: {}, Renda Média: {}, Escolaridade: {}, Trabalho Assalariado: {}"
                      .format(tribo[0], tribo[1], tribo[2], tribo[3], tribo[4], tribo[5]))
    except mysql.connector.Error as err:
        print("Erro ao listar as tribos: {}".format(err))
    finally:
        cursor.close()
        conn.close()
def atualizar_tribo():
    listar_tribos()
    id_tribo = int(input("Digite o ID da tribo que deseja atualizar: "))
   
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
       
        cursor.execute("SELECT * FROM tribos WHERE id = {}".format(id_tribo))
        tribo = cursor.fetchone()
       
        if not tribo:
            print("Tribo não encontrada.")
        else:
            print("Tribo selecionada:")
            print("ID: {}, Nome: {}, Habitantes: {}, Renda Média: {}, Escolaridade: {}, Trabalho Assalariado: {}"
                  .format(tribo[0], tribo[1], tribo[2], tribo[3], tribo[4], tribo[5]))
           
            nome = input("Novo nome da tribo: ")
            habitantes = int(input("Novo número de habitantes: "))
            renda_media = float(input("Nova renda média mensal: "))
            escolaridade = input("Nova escolaridade (fundamental, médio ou superior): ")
            trabalho_assalariado = input("Possui novo trabalho assalariado (sim ou não): ")
           
            sql = """
                UPDATE tribos
                SET nome_tribo = %s, num_habitantes = %s, renda_media = %s, escolaridade = %s, trabalho_assalariado = %s
                WHERE id = %s
            """
            data = (nome, habitantes, renda_media, escolaridade, trabalho_assalariado, id_tribo)
           
            cursor.execute(sql, data)
            conn.commit()
           
            print("Tribo atualizada com sucesso!")
           
    except mysql.connector.Error as err:
        print("Erro ao atualizar a tribo: {}".format(err))
    finally:
        cursor.close()
        conn.close()

# Função para excluir uma tribo do banco de dados
def excluir_tribo():
    listar_tribos()
    id_tribo = int(input("Digite o ID da tribo que deseja excluir: "))
   
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
       
        cursor.execute("SELECT * FROM tribos WHERE id = {}".format(id_tribo))
        tribo = cursor.fetchone()
       
        if not tribo:
            print("Tribo não encontrada.")
        else:
            confirmacao = input("Tem certeza que deseja excluir a tribo selecionada? (s/n): ")
            if confirmacao.lower() == "s":
                cursor.execute("DELETE FROM tribos WHERE id = {}".format(id_tribo))
                conn.commit()
                print("Tribo excluída com sucesso!")
            else:
                print("Exclusão cancelada.")
               
    except mysql.connector.Error as err:
        print("Erro ao excluir a tribo: {}".format(err))
    finally:
        cursor.close()
        conn.close()

# Menu principal
def menu():
    print("-----informações sobre tribos nativas brasileiras-----")
    print("1. Inserir tribo")
    print("2. Listar tribos")
    print("3. Atualizar tribo")
    print("4. Excluir tribo")
    print("0. Sair")
   
    while True:
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            inserir_tribo()
        elif opcao == "2":
            listar_tribos()
        elif opcao == "3":
            atualizar_tribo()
        elif opcao == "4":
            excluir_tribo()
        elif opcao == "0":
            print("Finalizando")
            break
        else:
            print("Opção inválida. Digite um número válido.")
        print()

# Execução do programa
menu()
import mysql.connector
