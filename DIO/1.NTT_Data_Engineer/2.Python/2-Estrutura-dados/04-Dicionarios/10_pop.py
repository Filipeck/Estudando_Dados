contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'} <- retorna o valor que removeu
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {} <- neste caso como não encontrou valor, retorna vazio, podemos passar qualquer valor de retorno para ele retornar
outro_exemplo = contatos.pop("guilherme@gmail.com", 'Não encontrado')
print(resultado)
print(outro_exemplo)
