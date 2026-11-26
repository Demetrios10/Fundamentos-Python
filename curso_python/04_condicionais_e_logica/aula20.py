"""Aula 20: operador or e validação de uma letra."""


def eh_letra_unica(texto):
    return len(texto) == 1 and texto.isalpha()


def main():
    letra = input("Digite uma letra: ").strip().casefold()
    if not eh_letra_unica(letra):
        print("Entrada inválida: informe uma única letra.")
    # O encadeamento de "or" é o assunto da aula; em código real, prefira "in".
    elif letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":  # noqa: PLR1714
        print("Vogal")
    else:
        print("Letra que não é uma das vogais a, e, i, o, u.")


if __name__ == "__main__":
    main()
