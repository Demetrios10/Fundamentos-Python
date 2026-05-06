from matplotlib import pyplot as plt

# graficos de barras 
eixo_x_dias = [1,5,10,15,20,25,30]
eixo_y_temp_max = [28,29,25,32,34,36,31]
eixo_y_temp_min = [8,9,10,11,12,13,14]

plt.title('Temperaturas máximas e mínimas')
plt.xlabel('Data atual')
plt.ylabel('Temperatura')


plt.bar(eixo_x_dias,eixo_y_temp_max,label='Tem Max')
plt.bar(eixo_x_dias,eixo_y_temp_min,label='Temp Min')

plt.legend(loc='best')
# plt.grid(True)

# plt.axis([1,31,5,45])
plt.xlim([1,31])
plt.xlim([-5,50])
print(plt.axis())
# plt.savefig('meu_grafico.png') salva o grafico
plt.show()
