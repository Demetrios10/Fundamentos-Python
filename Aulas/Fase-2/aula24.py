
"""
CONSTANTE = "variaveis" que não vão mudar
Muitas condições no mesmo if (ruim)
  <- Contagem de complexidade (ruim)
"""


velocidade = 61
local_carro = 110

radar_1 = 60
local_1 = 100 
radar_range = 1

velocidade_carro_passou_radar_1 = velocidade > radar_1
carro_multado_radar_1 = local_carro >= (local_1 - radar_range) and local_carro <= (local_1 + radar_range)

if velocidade_carro_passou_radar_1:
  print('Velocidade carro passou do radar 1')
  
if carro_multado_radar_1 and velocidade_carro_passou_radar_1:
  print('carro multado em radar 1')