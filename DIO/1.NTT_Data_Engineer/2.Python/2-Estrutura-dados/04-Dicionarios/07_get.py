contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError <- neste caso o programa para, pois não existe essa chave no dicionário

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {} <- se não achar a chave retorne um dicionário vazio
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"} <- neste caso ele encontrou a chave, então retorna ela em vez de vazio
print(resultado)
