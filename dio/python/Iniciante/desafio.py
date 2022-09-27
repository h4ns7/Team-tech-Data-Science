
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:




ICM = distancia/(diametro1+diametro2)

print(f'o ICM da comunicação dos Palantír é de {ICM:.2f}')
print(entrada)
print(diametro1)
print(diametro2)
print(distancia)