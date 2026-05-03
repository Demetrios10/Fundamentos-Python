# Jogo da palavra Completa 
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:

    letra = (input('Digite uma letra: '))
    numero_tentativas += 1

    if len(letra) > 1:
        print('Digite uma letra.')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
           palavra_formada += letra
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)


    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABENS')
        print('A Palavra era:',palavra_secreta)
        print('Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0







