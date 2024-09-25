salario = 2000

def salario_bonus(bonus,lista):
    global salario # informamos que a variavel usada dentro da função tem escopo global
    salario += bonus
    return salario

salario_bonus(500)