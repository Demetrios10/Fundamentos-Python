"""Aula 32: operadores de atribuição composta."""


def main():
    contador = 10
    contador += 2
    print(contador)  # 12
    contador -= 2
    print(contador)  # 10
    contador *= 3
    print(contador)  # 30
    contador /= 2
    print(contador)  # 15.0
    contador //= 2
    print(contador)  # 7.0
    contador **= 2
    print(contador)  # 49.0
    contador %= 5
    print(contador)  # 4.0


if __name__ == "__main__":
    main()
