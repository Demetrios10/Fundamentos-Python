"""Aula 29: flags e None."""


def main():
    resultado = None
    processar = True
    if processar:
        resultado = "Processamento concluído"
    if resultado is None:
        print("Ainda não há resultado.")
    else:
        print(resultado)


if __name__ == "__main__":
    main()
