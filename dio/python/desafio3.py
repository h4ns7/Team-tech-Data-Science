valores = input().split()

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal

tempo = int(valores[0])
velocidade = int(valores[1])

gasto = (tempo * velocidade)/12

print(f'{gasto:.3f}')
