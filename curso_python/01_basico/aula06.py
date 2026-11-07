"""Aula 06: conversão explícita de tipos."""


def main():
    print(10 + 10.0)  # int + float produz float
    print("D" + str(10))  # A conversão permite concatenar texto e número.
    inteiro = int("1")
    decimal = float("1.7")
    print(inteiro, type(inteiro))
    print(decimal, type(decimal))
    print(bool("texto"), type(bool("texto")))


if __name__ == "__main__":
    main()
