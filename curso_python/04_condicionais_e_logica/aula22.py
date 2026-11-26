"""Aula 22: operador in (pertence a)."""

NOMES_CADASTRADOS = ("Maria", "João", "Pedro", "Ana", "Carla")


def main():
    nome = input("Digite seu nome: ")

    if nome in NOMES_CADASTRADOS:
        print("Nome encontrado!")
    else:
        print("Nome não encontrado!")


if __name__ == "__main__":
    main()
