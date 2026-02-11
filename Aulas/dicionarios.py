# Dicionários

frutas = {
    'fruta 1': 'Laranja',
    'fruta 2': 'Manga',
    'fruta 3': 'Goiaba',
    'fruta 4': 'Melancia'
}
print(f'A Fruta é: {frutas['fruta 3']}') # mostra a fruta de numero 3 do dicionário
print(f'Nós Temos: {len(frutas)} frutas no total!!') # verifica quel total de itens tem no dicionário

# # atualizar uma entrada
# frutas['fruta 4'] = 'uva'
# print(frutas)

# # Adicionar uma entrada
# frutas['Fruta 5'] = 'jaboticaba'
# print(frutas)

# # Exclusão de itens em dicionários
# del frutas['fruta 4']
# print(frutas)

# # Apagar todos os itens 
# frutas.clear()
# print(frutas)

# # Apaga todo o dicionário da memoria 
# del frutas
# print(frutas)

for i,j in frutas.items():
    print(f'{i}: {j}')