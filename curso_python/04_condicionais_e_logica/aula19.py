"""Aula 19: operador and. Senha fictícia, apenas para estudo."""

RESPOSTAS_SIM = ("s", "sim")
SENHA_DEMONSTRACAO = "95120"


def main():
    entrada = input("Digite [S]im ou [N]ão: ").strip().casefold()
    senha = input(f"Senha de demonstração ({SENHA_DEMONSTRACAO}): ")
    if entrada in RESPOSTAS_SIM and senha == SENHA_DEMONSTRACAO:
        print("Entrar")
    else:
        print("Sair")


if __name__ == "__main__":
    main()
