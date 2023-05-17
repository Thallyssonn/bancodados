
import mysql.connector

# Configurações do banco de dados
config = {
    'user': 'admin',
    'password': 'aulanoiteFaculdade',
    'host': 'dbaula.cka0to8kgrtd.us-east-1.rds.amazonaws.com',
    'database': 'africa'
}

# Função para inserir informações sobre animais
def inserir_animal():
    raca = input("Raça do animal: ")
    quantidade = int(input("Quantidade: "))
    risco_extincao = input("Risco de extinção (sim ou não): ")
    area_encontrada = input("Área onde é encontrado (norte, sul, leste ou oeste): ")

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        sql = """
            INSERT INTO animais (raca, quantidade, risco_extincao, area_encontrada)
            VALUES (%s, %s, %s, %s)
        """
        data = (raca, quantidade, risco_extincao, area_encontrada)
        cursor.execute(sql, data)
        conn.commit()
        print("Informações do animal cadastradas com sucesso!")
    except mysql.connector.Error as err:
        print("Erro ao inserir informações do animal: {}".format(err))
    finally:
        cursor.close()
        conn.close()

# Função para listar informações de todos os animais cadastrados
def listar_animais():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animais")
        animais = cursor.fetchall()
        if not animais:
            print("Nenhum animal encontrado.")
        else:
            for animal in animais:
                print("ID: {}, Raça: {}, Quantidade: {}, Risco de Extinção: {}, Área Encontrada: {}"
                      .format(animal[0], animal[1], animal[2], animal[3], animal[4]))
    except mysql.connector.Error as err:
        print("Erro ao listar animais: {}".format(err))
    finally:
        cursor.close()
        conn.close()

# Menu principal
def menu():
    print("----- Animais Nativos Africanos-----")
    print("1. Inserir informações do animal")
    print("2. Listar animais")
    print("0. Sair")

    while True:
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            inserir_animal()
        elif opcao == "2":
            listar_animais()
        elif opcao == "0":
            print("Finalizando")
            break
        else:
            print("Opção inválida. Digite um número válido.")
        print()

# Execução do programa
menu()