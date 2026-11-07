"""Exemplo independente de fundamentos de Python."""


def main():
    # Operador = in = esta em

    nome = input('Digite seu nome: ')
    lista_nome = ['Maria', 'João', 'Pedro', 'Ana' , 'Carla']

    if nome in lista_nome:
        print('Nome encontrado!')
    else:
        print('Nome não encontrado!')


if __name__ == "__main__":
    main()
