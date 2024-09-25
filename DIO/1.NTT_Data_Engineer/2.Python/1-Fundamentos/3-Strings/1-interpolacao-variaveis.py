# OLD STYLE %
# %s para strings, %d para inteiros e %f para floats
nome = 'Filipe'
idade = 33
profissao = 'Analista de Dados'
linguagem = 'Python'

dados = {'nome': 'Filipe', 'idade': 33}
saldo = f'{17635:_.2f}'.replace('.',',').replace('_', '.')

print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' % (nome, idade, profissao, linguagem))

# Método format

print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))

print('Olá, me chamo {1}. Eu tenho {2} anos de idade, trabalho como {3} e estou matriculado no curso de {0}.'.format(linguagem, nome, idade, profissao))

print('Olá, me chamo {n}. Eu tenho {i} anos de idade, trabalho como {p} e estou matriculado no curso de {l}.'.format(l=linguagem, n=nome, i=idade, p=profissao))

#format com dicionário
print('Nome {nome} Idade {idade}'.format(**dados))

# f-string

print(f'Nome: {nome}, Idade: {idade}, Profissão {profissao}.')
print(f'Cliente: {nome} | Saldo: R${saldo}')