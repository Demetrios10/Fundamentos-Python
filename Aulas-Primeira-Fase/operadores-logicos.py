# Operadores Logicos 

# AND 
# OR 
# NOT 

# Participação em Evento 
idade = 25
altura = 1.79

resultado = (idade >= 18) and (altura >= 1.80)
msg = "Pode Participar do Evento ? " + str(resultado)
print(msg)


# Programa de Disparo de Alarme 
porta = 'a'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = "Alarme disparado ? " + str(alarme)
print(msg)


# Pode fazer Compra 
tem_dinheiro = True
tem_dinheiro = not tem_dinheiro
msg = 'Tem Dinheiro ? ' + str(tem_dinheiro)
print(msg)