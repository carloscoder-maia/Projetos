import requests

print('Conversor de moedas')
valor = float(input('Digite o valor em reais que deseja converter: '))

url = 'https://open.er-api.com/v6/latest/USD'

resposta = requests.get(url)
dados = resposta.json()
dolar = dados['rates']['BRL']

resultado = valor / dolar 

print(f'O valor de R${valor:.2f} convertido em dólares é igual a ${resultado:.2f}')

print('Conversão concluída com sucesso!')