# introdução a fStrings

nome = "Demetrios"
altura = 1.80000

linha1 = "Ola meu nome é " + nome + " e eu tenho " + str(altura) + " de altura"

# fString é uma forma mais simples e legível de formatar strings ,
# onde o operador f é utilizado para indicar que a
# string é uma fString e as variaveis são colocadas entre chaves {} dentro da string
linha2 = f'Ola Boa Tarde meu nome é {nome} e eu tenho {altura:.2f} de altura'

print(linha1)
print(linha2)
