texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=' ')
else:
    print("\nSim, existe else no FOR, porém muito menos usado.")


# função Buiilt-in range

for numero in range (0,51,5): # (start-inclusivo, stop-exclusivo, step-opcional)
    print(numero, end=' ')
