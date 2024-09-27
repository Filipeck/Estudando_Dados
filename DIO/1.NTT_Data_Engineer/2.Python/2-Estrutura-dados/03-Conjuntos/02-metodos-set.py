# .union()
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

uniao = conjunto_a.union(conjunto_b)
print(uniao)

# .intersection()
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)

# .difference()
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# .symmetric_difference() (todos os elementos que não estão na interseção)
print(conjunto_a.symmetric_difference(conjunto_b))

# .issubset() - verifica se todos elementos de um conjunto estão em outro conjunto (se ele é um subset, ou seja está incluso em)
conjunto_c = {1, 2, 3, 4}
conjunto_d = {4, 1, 2, 5, 6, 3}

print(conjunto_c.issubset(conjunto_d))
print(conjunto_d.issubset(conjunto_c))

# .issuperset() # verifica se todos os elementos de um conjunto estão no outro (se ele é um superset, ou seja se o conjunto em parenteses está contido nele)
print(conjunto_c.issuperset(conjunto_d))
print(conjunto_d.issuperset(conjunto_c))

# .isdisjoint() quando os dois conjuntos não possuem elementos em comum
conjunto_e = {1, 6, 7, 8}

print(conjunto_b.isdisjoint(conjunto_d)) # ou seja, tem elementos do b que estão no d
print(conjunto_b.isdisjoint(conjunto_e))

# .add()
sorteio = {1, 23}

sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25) # lembrando que set não permite duplicata
print(sorteio)

# .copy() copia o set
sorteio_2 = sorteio.copy()
print('Cópia:', sorteio_2)

# .clear() - limpa todo o set
sorteio_2.clear()
print('Cópia após .clear():', sorteio_2)

# .discard() elimina o item especificado do set
sorteio.discard(25)
print(sorteio)

# .pop() elimina o primeiro item do set
set_pop = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_pop.pop()
set_pop.pop()
set_pop.pop()
print('Conjunto após 3 .pop()', set_pop)

# .remove() ao contrário do pop, você especifica qual o elemento a ser retirado, ao contrário do discard se você passar um elemento que não exista no conjunto, retornará um erro
set_pop = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_pop.remove(4)
set_pop.remove(8)
print('Conjunto após 2 .remove()', set_pop)

# len() - mesmo uso de sempre, retorna o tamanho do conjunto
# in - verifica se um objeto está dentro do conjunto