"""Aula 17: uso do debugger para acompanhar o código linha por linha."""

NOME_ESPERADO = "Demetrios"


def main():
    nome = input("DIGITE SEU NOME: ").strip()

    if not nome:
        print("Nenhum nome digitado")
    elif nome == NOME_ESPERADO:
        print("Esse nome esta correto!!")
    else:
        print("Nome diferente do esperado!!")


if __name__ == "__main__":
    main()
