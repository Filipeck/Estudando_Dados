# def nomefuncao(argumento_posicional, / , argumento_posicional_ou_keywordarg, *, apenas_keywordarg)
#  quando usamos / após ela os argumentos podem ser posicionais ou kwargs, quando usamos * só podem argumentos kwargs


def armazenar_veiculo(modelo, ano, placa, /, marca, motor, combustivel): # a barra significa que antes dela é obrigatorio ser parametro posicional e após ela aceita posicional ou keyargs (kwargs), lembrando que são obrigatórios, o * permite apenas keyargs após ele
    print(modelo, ano, placa, marca, motor, combustivel)


# armazenar_veiculo('Palio', 1999, "ABC-8978", "Fiat", motor=1.0, combustivel="Gasolina") # válido

# armazenar_veiculo(modelo='Palio',ano=1999,placa="ABC-8978",marca='Fiat',motor=1.0, combustivel="Gasolina") # inválido, pois passamos keywords arguments quando definimos que são apenas argumentos posicionais

# only keywords args

def banco_veiculos(*, modelo, ano, placa):
    print(modelo, ano, placa)

# banco_veiculos("Palio", 1999, "ABC-4178") # inválido, pois neste caso por usarmos o * todos os argumentos que virão após ele precisam obrigatoriamente ser kwargs
banco_veiculos(modelo='Palio',ano=1999,placa='ABC-7777') # válido

# ultimo exemplo combinados
def criar_carro(modelo, ano, /, placa, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Uno", '2001', 'CDE-2556', marca='Fiat', motor='1.0',combustivel='Flex') # neste caso a marca poderia ser positional ou kwarg por exemplo