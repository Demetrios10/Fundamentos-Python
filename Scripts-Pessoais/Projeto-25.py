# varias formas de saida com o nome de cor 

cor = input('Digite uma cor: ')

if cor:
    print(f'A Cor digitada é: {cor}')
    print(f'O nome da cor invertido é: {cor[::-1]}')
    print(f'A letra inicial da cor, começa com: {cor[0]}')
    print(f'A letra da cor termina com: {cor[-1]}')
    print(f'A cor digitada tem: {len(cor)} letras')
    
    if ' ' in cor:
        print('Existe um espaço no nome da cor!!')
    else:
        print('Não existe espaços no nome da cor digitado!!')

else:
    print('Desculpa existe campos vazios!!')