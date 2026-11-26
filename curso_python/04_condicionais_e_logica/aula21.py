"""Aula 21: operador lógico not. Senha fictícia, apenas para estudo."""

SENHA_CORRETA = "123456"


def main():
    senha = input("Digite a senha: ")

    if not senha:
        print("Você não digitou nada")
    elif senha == SENHA_CORRETA:
        print("Você digitou a senha correta")
    else:
        print("Você digitou a senha incorreta")


if __name__ == "__main__":
    main()
