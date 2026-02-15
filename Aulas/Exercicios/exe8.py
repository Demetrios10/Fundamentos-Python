hora = (input('Digite uma hora em numeros inteiros: '))

try:
    horas = int(hora)
    
    if horas >= 0 and horas <= 11:
        print('Bom dia')
    elif horas >= 12 and horas <= 17:
        print('Boa tarde')
    elif horas >= 18 and horas <= 23:
        print('Boa noite')
    else:
        print('não conheço essa hora')
except:
    print('Por favor,digite apenas numeros inteiros')