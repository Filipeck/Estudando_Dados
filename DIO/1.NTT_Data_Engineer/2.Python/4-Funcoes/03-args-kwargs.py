def exemplo_args_kwargs(arg1, *args, **kwargs):
    print("Primeiro argumento:", arg1)
    
    print("\nArgumentos adicionais (args):")
    for arg in args:
        print(arg)
    
    print("\nArgumentos nomeados (kwargs):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Chamando a função com diferentes tipos de argumentos
exemplo_args_kwargs('primeiro', 'segundo', 'terceiro',1987, True, chave1='valor1', chave2='valor2', amor='Luciana')

# arg1 é um argumento posicional obrigatório.
# *args permite passar um número variável de argumentos posicionais.
# **kwargs permite passar um número variável de argumentos chaves nomeados.
