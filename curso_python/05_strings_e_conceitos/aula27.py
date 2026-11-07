# variaveis , constantes, complexibilidade de codigo

# radar de velocidade

velocidade = 200 # velocidade atual do carro
local_carro = 200 # local onde o carro esta
local_radar = 150 # local onde o radar esta
velocidade_radar = 60 # velocidade permitida no radar

if local_carro > local_radar and velocidade > velocidade_radar:
    print('carro multado')
else:
    print('carro dentro do limite de velocidade')




