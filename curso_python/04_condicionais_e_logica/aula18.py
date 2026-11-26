"""Aula 18: operadores de comparação (relacionais).

>  maior            <  menor
>= maior ou igual   <= menor ou igual
== igual            != diferente
"""


def main():
    # Comparações entre literais são intencionais: o objetivo é ver o resultado.
    print(2 > 10)  # noqa: PLR0133
    print(10 < 200)  # noqa: PLR0133
    print(1000 >= 1000)  # noqa: PLR0133
    print(200 <= 20)  # noqa: PLR0133
    print(10 == 10)  # noqa: PLR0133
    print("Demetrios" != "Deltas")  # noqa: PLR0133

    print("Deltas" == "Deltassss")  # noqa: PLR0133
    print("nome" != "Nomes")  # noqa: PLR0133


if __name__ == "__main__":
    main()
