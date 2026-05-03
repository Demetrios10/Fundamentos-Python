import matplotlib.pyplot as plt

cidade_a = [32,30,27,28,29,24]
cidade_b = [27,26,29,25,22,22]
cidade_c = [27,26,29,20,25,26]

datas = [5,10,15,20,25,30]

# criar posições distintas para cada cidade 
posicoes_a = list(range(len(datas)))
posicoes_b = [pos + 0.25 for pos in posicoes_a]
posicoes_c = [pos + 0.50 for pos in posicoes_a]

plt.bar(posicoes_a,cidade_a, width=0.25,color='red',label='Cidade A')
plt.bar(posicoes_b,cidade_b, width=0.25,color='blue',label='Cidade B')
plt.bar(posicoes_c,cidade_c, width=0.25,color='g',label='Cidade C')

plt.legend()
plt.xticks(ticks=posicoes_a,labels=datas)

plt.show()