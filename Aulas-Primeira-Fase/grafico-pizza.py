import matplotlib.pyplot as plt

linguagens = ['Python','Java','C#','Ruby']
quantidades = [300,270,150,40]
cores = ('#660033','blue','yellow','g')
distancia = (0, 0 , 0.2 , 0)

plt.pie(quantidades,colors=cores,labels=linguagens,explode=distancia,shadow=True,autopct='%1.1f%%',startangle=180)

plt.title('Preferencias de linguagens de programação')
plt.legend(title='Linguagens',loc='best',bbox_to_anchor=(1,0.9))
plt.show()