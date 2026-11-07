"""Aula 27: constantes e condições de um radar simplificado."""


def main():
    LIMITE_VELOCIDADE = 60
    POSICAO_RADAR = 150
    velocidade = 200
    posicao_carro = 200
    # Neste exercício, só verificamos o carro exatamente na posição do radar.
    if posicao_carro == POSICAO_RADAR:
        if velocidade > LIMITE_VELOCIDADE:
            print("Acima do limite no ponto de medição.")
        else:
            print("Dentro do limite no ponto de medição.")
    else:
        print("Carro fora do ponto de medição; sem avaliação de velocidade.")


if __name__ == "__main__":
    main()
