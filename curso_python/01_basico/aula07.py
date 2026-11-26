"""Aula 07: variáveis armazenam valores para reutilização.

Use nomes significativos para facilitar a leitura do código.
"""


def main():
    nome_completo = "Demetrios Alves Da Silva"
    print(nome_completo)

    soma_dois_numeros = 10 + 20
    print(soma_dois_numeros)

    # str() converte o número para que ele possa ser concatenado ao texto.
    print(nome_completo + " tem " + str(soma_dois_numeros) + " anos")

    nome = "Demetrios"
    idade = 39
    cidade = "São Paulo"
    maior_de_idade = True

    print(" o nome dele é " + nome)
    print(" ele tem " + str(idade) + " anos")
    print(" ele mora em " + cidade)
    print(" Ele é maior de idade ? " + str(maior_de_idade))


if __name__ == "__main__":
    main()
