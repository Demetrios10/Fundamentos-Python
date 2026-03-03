# Escopo Global e Local 

# Em Python, variáveis globais são definidas fora de funções e acessíveis em todo o programa. 
# Variáveis locais são criadas dentro de funções e limitadas ao seu escopo, 
# existindo apenas durante a execução daquela função. Variáveis locais ocultam as 
# globais com o mesmo nome dentro do seu escopo. 

# Aqui estão os detalhes principais:


# Variável Global:
# Definida fora de qualquer função ou classe.
# Acessível em qualquer parte do código (funções, classes, script principal).
# Para modificar uma variável global dentro de uma função, é necessário usar a palavra-chave global.


# Variável Local:
# Definida dentro de uma função ou método.
# Acessível apenas dentro da função onde foi criada.
# Destruída após a finalização da função. 

var_global = "Curso completo de Python"


def escreve_texto():
    global var_global # comando que permite acessar a variavel global fora da função 
    var_global = 'Bancos de dados com SQL' 
    var_local = "Demetrios Alves"
    print(f'Variavel Global: {var_global}')
    print(f'Variavel Local: {var_local}')

if __name__=='__main__':
    print(f'Escreve a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variaveis diretamente')
    print(f'Variavel Global:{var_global}')
    #vprint(f'Variavel Local:{var_local}') # só é acessivel dentro da função 

