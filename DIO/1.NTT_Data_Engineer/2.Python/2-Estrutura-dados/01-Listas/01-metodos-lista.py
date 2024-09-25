# .append()

lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)

# .copy() faz uma cópia da lista, mantendo a original intacta

lista_2 = lista.copy()

print(id(lista_2), id(lista))

lista_2[1] = "Luciana"

print(lista, lista_2, sep='\n')

# .clear() limpa a lista

lista_2.clear()

print(lista_2)

# .count() conta quantas vezes um objeto aparece na lista

cores = ['red', 'blue', 'green', 'red']

print(cores.count('red')) # 2

# .extend() é usado para adicionar todos os elementos de um iterável (como uma lista, tupla ou string) ao final de uma lista existente. Diferente do .append(), que adiciona um único elemento, o .extend() adiciona múltiplos elementos de uma vez. Ele não exclui duplicatas

linguagens = ["python", "js", "c"]

linguagens.extend(["java", "csharp", 'js', "python"])

print(linguagens)

# .index() verifica qual a primeira ocorrência do objeto especificado

linguagens.index("java") # 3

# .pop() por padrão remove o último objeto da lista, se passarmos o índice ele irá remover o índice citado
# .remove() ao contrário do .pop() é passado o objeto que deseja remover, caso exista mais de uma ocorrência do objeto ele irá remover o primeiro encontrado e assim por sequência

linguagens_2 = linguagens.copy()
print(linguagens_2)
linguagens_2.pop() # removeu 'python'
linguagens_2.pop(2) # removeu 'c'
linguagens_2.remove("js") # removeu o primeiro js, no index 1

print (linguagens_2)

# .reverse() inverte a ordem da lista (transpõe)
print(linguagens)
linguagens.reverse()
print(linguagens)

# .sort() ordena em 'ordem alfabética' o objeto lista
print(linguagens.sort())
print(linguagens.sort(reverse=True))
print(linguagens.sort(key=lambda x: len(x)))
print(linguagens.sort(key=lambda x: len(x), reverse=True))

# .len() retorna o tamanho do objeto, quantos elementos têm nela

print(len(linguagens))