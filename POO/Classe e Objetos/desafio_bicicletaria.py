# palavra reservada class para definir uma classe em python
class Bicicleta:
    # passando os parametros para o metodo construtor da classe
    # o argumento self representa a instancia do objeto
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # metodos sao basicamente funcoes dentro de uma classe
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")
    # metodo para retornar os atribitos de forma mais legivel para o usuario
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    
# objeto 
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(f"""
cor da bicicleta:{b1.cor},
modelo da bicicleta:{b1.modelo},
ano da bicicleta: {b1.ano},
valor da bicicleta: {b1.valor}""")

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
#b2.correr()