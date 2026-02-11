# Escopo Global e Local 
var_global = "Curso Completo de Python"

def escreve_texto():
    var_local = "Demetrios"
    print(f'Variavel Global: {var_global}')
    print(f'Variavel local: {var_local}')


if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()


    print('Tentar acessar as variaveis diretamente')
    print(f'Variavel Global{var_global}')
