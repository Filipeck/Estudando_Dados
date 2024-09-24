def calcular_total(lista_numeros):
    return sum(lista_numeros)


def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor,sucessor

def func_3():
    print('Olá, mundo!')

print(calcular_total([10,20,34])) # 64
print(retorna_antecessor_sucessor(10)) # (9,11)
print(func_3()) # None - por padrão o comportamento é retornar None

