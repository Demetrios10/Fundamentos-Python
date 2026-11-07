"""Aula 15: if, elif e else com entrada normalizada."""


def main():
    entrada = input("Digite sim ou não: ").strip().casefold()
    if entrada in ("sim", "s"):
        print("Você digitou Sim")
    elif entrada in ("não", "nao", "n"):
        print("Você digitou Não")
    else:
        print("Resposta inválida. Digite sim ou não.")


if __name__ == "__main__":
    main()
