# Introdução a f-strings
#
# f-string: prefixo f antes das aspas; variáveis e expressões vão entre { }.
# Mais legível que concatenar com + e str().

nome = "Demetrios"
sobrenome = "Alves Da Silva"
bairro = "Socorro"
rua = "Nora Ney"
numero = 40

ficha_cadastral = 'O aluno {} {} mora no bairro: {} na rua: {} numero: {}'
formato = ficha_cadastral.format(nome,sobrenome, bairro ,rua , numero)
print(formato)


