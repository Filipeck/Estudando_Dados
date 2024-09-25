frutas = ['laranja', 'maçã', 'abacaxi']
print(frutas)

frutas =[]
print(frutas)

letras = list('python')
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]
print(carro)

# Fatiamento

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

# percorrendo com for

carros = ['Gol', "Celta", "Palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# List comprehension
# Filtro versão 1 (sem comprehension)

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Filtro versão 2

pares_2 = [numero for numero in numeros if numero % 2 == 0]

# modificando valores (sem comprehension)
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# modificando com comprehension

quadrado_2 = [numero ** 2 for numero in numeros]