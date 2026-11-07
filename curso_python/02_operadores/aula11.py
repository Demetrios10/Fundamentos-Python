"""Aula 11: precedência de operadores.

Parênteses agrupam expressões. ** precede *, /, // e %.
Esses operadores precedem + e -.
"""


def main():
    print(10 + 20 * 30)  # 610
    print((10 + 20) * 30)  # 900
    print(10 + 20 * 30 - 40)  # 570
    print(10 + 20 * 30 - 40 / 2)  # 590.0
    print(10 + 20 * 30 - 40 / 2 ** 2)  # 600.0
    print(10 + 30 * 10 - 30 / 10 ** 2)  # 309.7
    print(20 + 40 * 1 - 8 ** 1 // 3)  # 58


if __name__ == "__main__":
    main()
