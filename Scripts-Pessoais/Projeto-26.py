# seleção de cores 
while True:
    cor = input('Digite uma cor: ')
    
    cores_permitidas = ['laranja','amarelo','verde','roxo','preto','branco']
    
    if cor not in cores_permitidas:
        print('Não temos essa cor, selecione outra por favor.')
        continue
    if cor in cores_permitidas:
        print('Temos essa cor!!')
        print('vamos seguir com o projeto!!')

    sair = input('Deseja sair do sistema? [s]im: ').lower().startswith('s')
      
    if sair is True:
     print('vc saiu!!')
     break

  