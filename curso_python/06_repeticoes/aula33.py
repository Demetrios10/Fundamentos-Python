"""Exemplo independente de fundamentos de Python."""


def main():
    # while com continue

    numero = 0

    while numero < 100:
        numero += 1

        if numero == 40:
            print('Não mostre o numero 40')
            continue
        print(numero)


if __name__ == "__main__":
    main()
