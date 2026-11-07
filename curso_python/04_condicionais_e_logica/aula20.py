"""Aula 20: operador or e validação de uma letra."""


def main():
    letra = input("Digite uma letra: ").strip().casefold()
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida: informe uma única letra.")
    elif letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Vogal")
    else:
        print("Letra que não é uma das vogais a, e, i, o, u.")


if __name__ == "__main__":
    main()
