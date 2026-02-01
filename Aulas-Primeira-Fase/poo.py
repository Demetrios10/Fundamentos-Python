# Orinetação a Objetos: paradigma de programação
# Classes e Objetos 

class Veiculo: 
     def movimentar(self):
         print(f'Sou um veiculo e me desloco!')
    
     def __init__(self,fabricante,modelo):
         self.__fabricante = fabricante
         self.__modelo = modelo
         self.__num_registro = None
         
    # Getter 
     def get_fabr_modelo(self):
         print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
             
if __name__ =='__main__':
    meu_veiculo = Veiculo('GM','Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    