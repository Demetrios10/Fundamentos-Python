"""Aula 28: identidade e igualdade de objetos.

id identifica um objeto enquanto ele existe; não é um endereço garantido
em todas as implementações de Python.
"""


def main():
    primeira_lista = [1, 2]
    segunda_lista = [1, 2]
    mesma_lista = primeira_lista
    print(primeira_lista == segunda_lista)  # True: conteúdo igual.
    print(primeira_lista is segunda_lista)  # False: objetos diferentes.
    print(primeira_lista is mesma_lista)  # True: mesmo objeto.
    print(id(primeira_lista), id(segunda_lista))


if __name__ == "__main__":
    main()
