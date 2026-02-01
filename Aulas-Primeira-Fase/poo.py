# Orinetação a Objetos: paradigma de programação
# Classes e Objetos 

class Veiculo: 
     def movimentar(self):
         print(f'Sou um veiculo e me desloco!')
    
     def __init__(self,fabricante,modelo):
         self.__fabricante = fabricante
         self.__modelo = modelo
         self.__num_registro = None
    
    # Setter
     def set_num_registro(self,registro):
        self.__num_registro = registro
         
    # Getter 
     def get_fabr_modelo(self):
         print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
         
     def get_num_registro(self):
         return self.__num_registro
               
class Carro(Veiculo):
    # metodo __init__ sera herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')
        
class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Corro Muito')
    
if __name__ =='__main__':
#     meu_veiculo = Veiculo('GM','Cadillac Escalade')
#     meu_veiculo.movimentar()
#     meu_veiculo.get_fabr_modelo()
#     meu_veiculo.set_num_registro('490321-1')
#     print(f'Registro:{meu_veiculo.get_num_registro()}\n')
    
    meu_carro = Carro('Fiat','Uno')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()
    
    seu_carro = Carro('Audi','Q3')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()
    
    moto = Motocicleta('R1','Yamaha')
    moto.movimentar()
    moto.get_fabr_modelo()
    