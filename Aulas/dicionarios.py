# Dicionário 

elemento = {
    'Z':3,
    'nome':'Lítio',
    'grupo':'Metais Alcalinos',
    'densidade':0.534
}

print(f'Elemneto: {elemento['nome']}') # printando somente um elemento na saida de dados 
print(f'Densidade: {elemento['densidade']}') # printando somente um elemento na saida de dados 
print(f'O dicionario possui {len(elemento)} elementos') # contando quantos elementos possuem no dicionario 

elemento ['grupo'] = 'Deltas' # Trocando um elemento no dicionario 
print(elemento)