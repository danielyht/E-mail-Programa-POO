from models import Remetente, Destinatario, Email, EmailDestinatario
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    limpar()
    print("------------------------")
    print("------ Menu Email ------")
    print("------------------------")
    print("1. Remetente")
    print("2. Destinatário")
    print("3. Email")
    print("0. Sair")
    opc = int(input("Opção: "))
    print("------------------------\n")

    if opc == 0:
        print("Encerrando o programa...")
        break

    elif opc == 1:
        print("Menu de Remetente")
        print("1. Cadastrar")
        print("2. Listar")
        opc2 = int(input("Opção: "))
        print("")

        if opc2 == 1:
            print("Cadastrando um remetente...")
            nome = input("Nome: ")
            email = input("Email: ")
            remetente = Remetente.create(nome=nome, emailAddress=email)
            print(f"Remetente {remetente.nome} cadastrado com sucesso!")

        elif opc2 == 2:
            print("Remetentes cadastrados:")
            lista = Remetente.select()
            for r in lista:
                print(f"ID: {r.id} - {r.nome} <{r.emailAddress}>")

        input("\nDigite ENTER para continuar...")

    elif opc == 2:
        print("Menu de Destinatário")
        print("1. Cadastrar")
        print("2. Listar")
        opc2 = int(input("Opção: "))
        print("")

        if opc2 == 1:
            print("Cadastrando um destinatário...")
            nome = input("Nome: ")
            email = input("Email: ")
            destinatario = Destinatario.create(nome=nome, emailAddress=email)
            print(f"Destinatário {destinatario.nome} cadastrado com sucesso!")

        elif opc2 == 2:
            print("Destinatários cadastrados:")
            lista = Destinatario.select()
            for d in lista:
                print(f"ID: {d.id} - {d.nome} <{d.emailAddress}>")

        input("\nDigite ENTER para continuar...")

    elif opc == 3:
        print("Menu de Emails")
        print("1. Criar e Enviar Email")
        print("2. Listar Emails Enviados")
        opc2 = int(input("Opção: "))
        print("")

        if opc2 == 1:
            print("Criando um email...")
            titulo = input("Título: ")
            corpo = input("Corpo do email: ")

            print("\n--- Escolha o remetente ---")
            for r in Remetente.select():
                print(f"{r.id}. {r.nome} <{r.emailAddress}>")
            id_rem = int(input("ID do Remetente: "))
            remetente = Remetente.get_by_id(id_rem)

            email = Email.create(titulo=titulo, corpo=corpo, remetente=remetente)

            print("\n--- Escolha os destinatários (ID separados por vírgula) ---")
            for d in Destinatario.select():
                print(f"{d.id}. {d.nome} <{d.emailAddress}>")
            ids_dest = input("IDs dos Destinatários: ").split(",")

            for id_d in ids_dest:
                try:
                    destinatario = Destinatario.get_by_id(int(id_d.strip()))
                    EmailDestinatario.create(email=email, destinatario=destinatario)
                except:
                    print(f"Destinatário com ID {id_d.strip()} não encontrado.")

            print(f"Email '{titulo}' enviado com sucesso!")

        elif opc2 == 2:
            print("Emails enviados:")
            for e in Email.select():
                print(f"\nTítulo: {e.titulo}")
                print(f"Corpo: {e.corpo}")
                print(f"Data: {e.dataEnvio.strftime('%d/%m/%Y %H:%M')}")
                print(f"Remetente: {e.remetente.nome} <{e.remetente.emailAddress}>")
                print("Destinatários:")
                for rel in e.destinatarios:
                    d = rel.destinatario
                    print(f" - {d.nome} <{d.emailAddress}>")

        input("\nDigite ENTER para continuar...")
