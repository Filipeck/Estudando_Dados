contatos = {
    "filipe@gmail.com": {"nome": "Filipe", "telefone": "3333-2221", 'amor': {'mozona': 'Luciana'}},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

amor = contatos["filipe@gmail.com"]["amor"]['mozona']
print(amor)
