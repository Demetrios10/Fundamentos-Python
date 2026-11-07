"""Aula 19: operador and. Senha fictícia, apenas para estudo."""


def main():
    entrada = input("Digite [S]im ou [N]ão: ").strip().casefold()
    senha = input("Senha de demonstração (95120): ")
    if entrada in ("s", "sim") and senha == "95120":
        print("Entrar")
    else:
        print("Sair")


if __name__ == "__main__":
    main()
