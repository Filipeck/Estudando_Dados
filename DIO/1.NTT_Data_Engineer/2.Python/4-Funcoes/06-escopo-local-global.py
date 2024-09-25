salario = 2000

def salario_bonus(bonus,lista):
    global salario # a palavra chave global permite utilizar variáveis globais no escopo da função sem receber a variável por argumento
    salario += bonus
    return salario

salario_bonus(500)