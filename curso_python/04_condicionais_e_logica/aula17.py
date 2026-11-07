"""Exemplo independente de fundamentos de Python."""


def main():
    # debugger
    # serve para verificação do código linha por linha

    nome = input('DIGITE SEU NOME: ').strip()

    if nome == '':
        print('Nenhum nome digitado')
    elif nome == 'Demetrios':
        print('Esse nome esta correto!!')
    else:
        print('Nome diferente do esperado!!')


if __name__ == "__main__":
    main()
