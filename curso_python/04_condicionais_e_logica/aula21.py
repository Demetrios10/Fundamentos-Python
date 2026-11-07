"""Exemplo independente de fundamentos de Python."""


def main():
    # Operador Logico = Not = Não

    senha = input('Digite a senha: ')

    if not senha:
        print('Você não digitou nada')
    elif senha == '123456':
        print('Você digitou a senha correta')
    else:
        print('Você digitou a senha incorreta')


if __name__ == "__main__":
    main()
