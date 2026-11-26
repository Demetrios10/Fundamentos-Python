"""Aula 23: operador not in e validação de uma letra."""

VOGAIS = ("a", "e", "i", "o", "u")


def eh_letra_unica(texto):
    return len(texto) == 1 and texto.isalpha()


def main():
    letra = input("Digite uma letra: ").strip().casefold()
    if not eh_letra_unica(letra):
        print("Entrada inválida: informe uma única letra.")
    elif letra not in VOGAIS:
        print("A letra não é uma das vogais a, e, i, o, u.")
    else:
        print("Vogal")


if __name__ == "__main__":
    main()
