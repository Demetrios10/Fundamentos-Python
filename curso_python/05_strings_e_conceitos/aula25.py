"""Aula 25: índices e fatiamento de strings."""


def main():
    nome = "Demetrios"
    print(nome[3])

    sobrenome = "Alves da silva"
    print(sobrenome[4])
    print(sobrenome[0:3])
    print(sobrenome[2:5])
    print(len(sobrenome))  # quantidade de caracteres
    print(sobrenome[0:9:2])  # [início:fim:passo] — um caractere a cada dois
    print(sobrenome[::-1])  # passo negativo percorre a string ao contrário


if __name__ == "__main__":
    main()
