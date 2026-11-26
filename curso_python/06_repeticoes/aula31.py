"""Aula 31: laço while."""

LIMITE = 10


def main():
    contador = 0

    while contador < LIMITE:
        print(f"Esse numero {contador} é menor que {LIMITE}:")
        contador += 1


if __name__ == "__main__":
    main()
