# Usado para verificar se um objeto ocupa o mesmo espaço de memória do outro

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)

limite = 1000

print(saldo is limite)
print(saldo is not limite)

texto = "Python é vida ~~~~:)"
texto_copia = texto

print(texto is texto_copia)
print(texto is not texto_copia)