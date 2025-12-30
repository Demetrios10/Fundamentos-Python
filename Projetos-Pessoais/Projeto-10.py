import random

novo_jogo = 's'

while novo_jogo == 's':
    print(f'Bem-Vindo ao Jogo de advinhação!')
    print(f'Voce tera tres chances para adivinhar um numero entre 1 e 15.')

    # Gerar o numero aleatorio secreto 
    num = random.randint(1,15)

    # Jogar 
    for i in range(3):
        print(f'\nQual a sua escolha ?')
        chute = int(input())

        if chute == num:
            print(f'Parabens, Voce acertou!')
            break
        elif chute > num:
            print(f'Numero alto')
        else:
            print(f'Numero baixo')

    # Caso não tenha acertado revelar o numero secreto 
    if chute != num:
        print(f'\nO numero secreto era o {num}')
    
    novo_jogo = input('Deseja Jogar outra vez? S para sim, outra tecla para não: ')
    novo_jogo = novo_jogo.lower()