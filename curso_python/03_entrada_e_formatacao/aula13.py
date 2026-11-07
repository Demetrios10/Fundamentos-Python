"""Aula 13: comparar str.format com f-strings; dados fictícios."""


def main():
    nome = "Pessoa"
    sobrenome = "Exemplo"
    cidade = "São Paulo"
    print("Nome: {} {}. Cidade: {}.".format(nome, sobrenome, cidade))
    print(f"Nome: {nome} {sobrenome}. Cidade: {cidade}.")


if __name__ == "__main__":
    main()
