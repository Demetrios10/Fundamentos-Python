# imprimindo nomes da lista com uma função 

def nomes(imprima):
    nomes = []
    for i in imprima:
        nomes.append(i)
    return nomes

if __name__=='__main__':
    NomesCompletos = ['Demetrios Alves','Marcia Santiago','Rodrigo Fonseca','Denis Fausto']
    resultado = nomes(NomesCompletos)
    for f in resultado:
        print(f'O nome completo que esta na lista é: {f}')

