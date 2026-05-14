# Introdução a f-strings
#
# f-string: prefixo f antes das aspas; variáveis e expressões vão entre { }.
# Mais legível que concatenar com + e str().

nome = "Demetrios"
sobrenome = "Alves da Silva"
altura = 1.8
cidade = "São Paulo"

nome_completo = f"{nome} {sobrenome}"

# Forma antiga (concatenação) — funciona, mas é verbosa e propensa a erro:
# linha_antiga = "Olá, meu nome é " + nome + " e eu tenho " + str(altura) + " de altura"

linha_saudacao = (
    f"Olá, boa tarde. Meu nome é {nome} e eu tenho {altura:.2f} m de altura."
)

linha_completa = (
    f"O nome completo é {nome_completo} e eu tenho {altura:.2f} m de altura."
)

if __name__ == "__main__":
    print(linha_saudacao)
    print(linha_completa)
    print(f"Moro em {cidade}.")
