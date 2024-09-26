# criando tupla

frutas = ('laranka', 'pera', 'uva',)

letras = tuple('python')
print(letras)

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)
print(pais)

# acessando itens - igual na lista

frutas[0] # laranja
frutas[-1] # uva

# tuplas aninhadas

matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 5, 'c'),
)

matriz[0] # (1, 'a', 2)
matriz[0][0] # 1
matriz[-1][1] # 5

# fatiamento tupla - que nem em lista

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

# iterar tupla

carros = ('gol', 'uno', 'celta',)

for carro in carros: 
    print(carro)