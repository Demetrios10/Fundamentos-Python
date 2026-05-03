# Token de Segurança 

Token_Reconhecimento = None

while True:
    Token_Reconhecimento = int(input('Digite Token: '))
    if(int(Token_Reconhecimento != 8534)):
     print('Digite Novamente!!')
    if(int(Token_Reconhecimento == 8534)):
     print('Você esta logado!!')
     break

