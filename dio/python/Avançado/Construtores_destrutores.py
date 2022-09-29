class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordade = acordado

    def __del__(self):
        print("Removendo instância da classe.")

    def falar(self):
        print("Auaua")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco", False)
    print(c.nome)

#c = Cachorro("Ayla", "Bege")
# c.falar()


criar_cachorro()
