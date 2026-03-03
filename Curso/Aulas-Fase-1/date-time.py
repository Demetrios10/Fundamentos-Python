# importe datetime ou time 

import datetime
import time

data = datetime.date(2026,1,11)
print(data)

data.year
print(data)

datetime.date.today()
print(datetime)

agora = datetime.datetime.today()
print(agora)
print(agora.strftime("%d/%m/%Y")) # Data 
print(agora.strftime("%H:%M:%S")) # Hora , Minuto , Segundo 

hoje = datetime.datetime.now()
festa = datetime.datetime(2026,11,1,19,00)
dias = festa - hoje 
print(f'Faltam Esses dias para a festa {dias}')

print(time.gmtime(0)) # Tempo de Criação do Sistema 
print(time.time)
