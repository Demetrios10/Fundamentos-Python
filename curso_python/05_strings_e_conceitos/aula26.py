"""Aula 26: tratar somente o erro esperado de conversão."""


def main():
    texto = input("Digite um número: ").strip().replace(",", ".")
    try:
        numero = float(texto)
    except ValueError:
        print("Entrada inválida: isso não é um número.")
    else:
        print(f"O dobro de {numero} é {numero * 2}.")


if __name__ == "__main__":
    main()
