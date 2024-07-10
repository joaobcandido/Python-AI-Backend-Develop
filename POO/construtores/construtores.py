class Cachorro:
    # é utilizado __init__ como construtor inicializador da classe
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    # é utilizado __del__ para deletar a instancia da classe
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)
    print(c.cor)
    print(c.acordado)

criar_cachorro()

