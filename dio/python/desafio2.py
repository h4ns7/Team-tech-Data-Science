valores = input().split()

# TODO:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.

hotdog = int(valores[0])
pessoa = int(valores[1])

media = hotdog/pessoa

print(f'{media:.2f}')
