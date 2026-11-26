"""Aula 33: while com continue para pular uma iteração."""

LIMITE = 100
NUMERO_IGNORADO = 40


def main():
    numero = 0

    while numero < LIMITE:
        numero += 1

        if numero == NUMERO_IGNORADO:
            print(f"Não mostre o numero {NUMERO_IGNORADO}")
            continue
        print(numero)


if __name__ == "__main__":
    main()
