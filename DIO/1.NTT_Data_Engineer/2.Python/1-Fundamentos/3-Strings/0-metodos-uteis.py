nome = "fILiPe cAYrEs"

print(nome.upper())
print(nome.lower())
print(nome.title())
print(nome.capitalize())

texto = '  Olá mundo!    '

print(texto)
print(texto.strip() + '.')
print(texto.lstrip() + '.')
print(texto.rstrip() + '.')

menu = 'Python'

print(menu.center(14, '#')) # segundo parâmetro é opional, por padrão ele preenche com espaço vazio
print('-'.join(menu))