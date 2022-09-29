# Desafio bicicletária

from distutils import core
from importlib.util import module_for_loader


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Plim Plim......")

    def parar(self):
        print("Parando a bike....")
        print("Bike parada!")

    def correr(self):
        print("Vrummmmmmmm...")

    def __str__(self):
        return f'Bicicleta: Cor = {self.cor}, Modelo = {self.modelo}, Ano = {self.ano}, Valor = {self.valor}'

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("Verde", "Monaco", 1990, 2000)
print(b1)
