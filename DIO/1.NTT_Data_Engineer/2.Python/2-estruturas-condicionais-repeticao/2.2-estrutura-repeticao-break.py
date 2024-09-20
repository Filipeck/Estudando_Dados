while True:
    numero = int(input('Informe um número: '))

    if numero == 10:
        break # enquanto não inserir 10 o loop continuará infinitamente
    if numero % 2 == 1:
        continue

    print(f'{numero} é par!')



for numero in range(100):

    if numero == 10:
        break

    print(numero, end=' ')


for numero in range(100):

    if numero % 2 == 0:
        continue # pula a execução

    print(numero, end=' ')