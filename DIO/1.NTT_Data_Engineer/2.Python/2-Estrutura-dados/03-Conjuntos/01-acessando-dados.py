# conjuntos em Python não suportam indexação e fatiamento, caso queira acessar seus valores é necessário converter o conjunto para lista

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros)

# iterando com for
carros = {'gol', 'celta', 'uno', 'palio'}

for carro in carros:
    print(carro)

# enumerate
carros = {'gol', 'celta', 'uno', 'palio'}

for indice, carro in enumerate(carros):
    print(indice, carro)