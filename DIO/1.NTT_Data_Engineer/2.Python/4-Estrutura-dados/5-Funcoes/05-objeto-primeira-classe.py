def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação é = {resultado}')

exibir_resultado(15, 17, somar) #não chamamos a função com () neste caso
exibir_resultado(15, 17, subtrair) #não chamamos a função com () neste caso


op = somar # por ser objeto de primeira classe, pode ser atribuido a variáveis também

print(op(1, 23))