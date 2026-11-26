"""Aula 02: a função print e seus parâmetros."""


def main():
    print(23, 44, 55)

    # sep define o separador entre os valores
    print(12, 34, sep="--")
    print(56, 78, sep="==")
    print(9, 10, sep="**")
    print("Demetrios", "Alves", sep="*")

    # \n pula para a próxima linha
    print("Olá, Mundo!\nBem-vindo ao Python.")

    # \r retorna o cursor para o início da linha
    print("Olá, Mundo!\rPython é incrível.")


if __name__ == "__main__":
    main()
