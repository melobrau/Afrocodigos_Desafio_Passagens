class PassagensAereasManager():

        def __init__(self):
            self.passagens_compradas = []
        
        def adicionar_passagem(self, passagem):
            self.passagens_compradas.append(passagem)

class Passagem:
    def __init__(self, origem, destino, valor):
         self.origem = origem
         self.destino = destino
         self.valor = valor 

         
    def __repr__(self):        
         return f"Passagem => De'{self.origem}', PARA'{self.destino}', PAGANDO={self.valor})"
