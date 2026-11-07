"""Aula 12: cálculo matemático de IMC, com validação de entrada."""
import math


def calcular_imc(peso, altura):
    if not all(math.isfinite(v) and v > 0 for v in (peso, altura)):
        raise ValueError("Peso e altura devem ser positivos e finitos.")
    return peso / altura ** 2


def main():
    nome = input("Digite o nome: ").strip()
    try:
        altura = float(input("Altura em metros: ").replace(",", "."))
        peso = float(input("Peso em kg: ").replace(",", "."))
        imc = calcular_imc(peso, altura)
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        return
    print(f"{nome}: IMC calculado = {imc:.2f}")


if __name__ == "__main__":
    main()
