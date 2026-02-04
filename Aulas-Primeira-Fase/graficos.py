from matplotlib import pyplot as plt

eixo_x_dias = [1,5,10,15,20,25,30]
eixo_y_temp_max = [28,29,25,32,34,36,31]
eixo_y_temp_min = [21,22,17,23,23,24,20]

plt.title('Temperaturas máximas e mínimas')
plt.xlabel('Data')
plt.ylabel('Temperatura')


plt.plot(eixo_x_dias,eixo_y_temp_max,linestyle='--',marker='o')
plt.plot(eixo_x_dias,eixo_y_temp_min,color='y',linestyle='--',marker='o')

plt.legend(['Temp Max','Temp Min'])
plt.grid(True)

plt.show()