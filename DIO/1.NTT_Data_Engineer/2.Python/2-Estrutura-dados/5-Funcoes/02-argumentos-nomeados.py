def armazenar_veiculo(marca, modelo, ano, placa):
    # salva o carro no banco de dados...
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')


# armazenar_veiculo("Fiat", "Palio", 1999, "ABC-1234")
# armazenar_veiculo(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
armazenar_veiculo(**{'marca': "Fiat", "modelo": 'Palio', 'ano': 1999, 'placa': 'ABC-1234'})
