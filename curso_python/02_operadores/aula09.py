"""Aula 09: operadores aritméticos."""


def main():
    numero1 = 20
    numero2 = 20

    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2
    divisao_inteira = numero1 // numero2
    resto = numero1 % numero2
    potencia = numero1**numero2

    print(soma)
    print(subtracao)
    print(multiplicacao)
    print(divisao)
    print(divisao_inteira)
    print(resto)
    print(potencia)

    # O operador % ajuda a verificar divisibilidade.
    print(10 % 8 == 0)  # False: o resto de 10 / 8 é 2
    print(10 % 5 == 0)  # True: 10 é divisível por 5

    joao_tem = 10
    maria_tem = 40

    print("A soma do valor dos dois é de: " + str(joao_tem + maria_tem))
    print("A subtração do valor dos dois é de: " + str(joao_tem - maria_tem))
    print("A multiplicação do valor dos dois é de: " + str(joao_tem * maria_tem))
    print("A divisão do valor dos dois é de: " + str(joao_tem / maria_tem))
    print("A divisão inteira do valor dos dois é de: " + str(joao_tem // maria_tem))
    print("O resto da divisão do valor dos dois é de: " + str(joao_tem % maria_tem))


if __name__ == "__main__":
    main()
