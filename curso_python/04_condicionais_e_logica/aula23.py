"""Aula 23: operador not in e validação de uma letra."""


def main():
    letra = input("Digite uma letra: ").strip().casefold()
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida: informe uma única letra.")
    elif letra not in ["a", "e", "i", "o", "u"]:
        print("A letra não é uma das vogais a, e, i, o, u.")
    else:
        print("Vogal")


if __name__ == "__main__":
    main()
