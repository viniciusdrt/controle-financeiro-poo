from datetime import date

from categoria import Categoria
from receita import Receita
from despesa import Despesa
from controle_financeiro import ControleFinanceiro


def exibir_menu():
    print("\n===== CONTROLE FINANCEIRO =====")
    print("1 - Cadastrar receita")
    print("2 - Cadastrar despesa")
    print("3 - Listar transações")
    print("4 - Consultar saldo")
    print("5 - Cadastrar categoria")
    print("6 - Listar categorias")
    print("7 - Ver situação financeira")
    print("8 - Sair")


def main():
    controle = ControleFinanceiro()
    categorias = []

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da receita: ")
            valor = float(input("Valor da receita: R$ "))
            
            if not categorias:
                print("Cadastre uma categoria primeiro.")
                continue

            print("\nCategorias:")
            for i, categoria in enumerate(categorias, start=1):
                print(f"{i} - {categoria.nome}")

            escolha = int(input("Escolha a categoria: "))
            categoria = categorias[escolha - 1]

            receita = Receita(
                descricao,
                valor,
                date.today(),
                categoria
            )

            controle.adicionarTransacao(receita)

            print("Receita cadastrada com sucesso!")

        elif opcao == "2":
            descricao = input("Descrição da despesa: ")
            valor = float(input("Valor da despesa: R$ "))

            if not categorias:
                print("Cadastre uma categoria primeiro.")
                continue

            print("\nCategorias:")
            for i, categoria in enumerate(categorias, start=1):
                print(f"{i} - {categoria.nome}")

            escolha = int(input("Escolha a categoria: "))
            categoria = categorias[escolha - 1]

            despesa = Despesa(
                descricao,
                valor,
                date.today(),
                categoria
            )

            controle.adicionarTransacao(despesa)

            print("Despesa cadastrada com sucesso!")

        elif opcao == "3":
            transacoes = controle.listarTransacoes()

            if not transacoes:
                print("Nenhuma transação cadastrada.")
            else:
                print("\n===== TRANSAÇÕES =====")

                for transacao in transacoes:
                    print(
                        f"{transacao.data} | "
                        f"{transacao.descricao} | "
                        f"R$ {transacao.valor:.2f} | "
                        f"{transacao.categoria.nome}"
                    )

        elif opcao == "4":
            saldo = controle.calcularSaldo()
            print(f"\nSaldo atual: R$ {saldo:.2f}")

        elif opcao == "5":
            nome = input("Nome da categoria: ")
            descricao = input("Descrição da categoria: ")

            categoria = Categoria(nome, descricao)
            categorias.append(categoria)

            print("Categoria cadastrada com sucesso!")

        elif opcao == "6":
            if not categorias:
                print("Nenhuma categoria cadastrada.")
            else:
                print("\n===== CATEGORIAS =====")

                for categoria in categorias:
                    print(
                        f"{categoria.nome} - "
                        f"{categoria.descricao}"
                    )

        elif opcao == "7":
            print(controle.verificarSituacao())

        elif opcao == "8":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
