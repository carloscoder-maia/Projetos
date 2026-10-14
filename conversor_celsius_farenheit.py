print('Conversor de Temperatura')

opcao = int(input('Digite 1 para converter de Celsius para Farenheit ou 2 para converter de farenheit para Celsius: '))

if opcao == 1:
    celsius = float(input('Digite a temperatura em Celsius: '))
    farenheit = (celsius * 1.8) + 32
    print(f'A temperatura em Farenheit é: {farenheit:.2f}')
elif opcao == 2:
    farenheit = float(input('Digite a temperatura em Farenheit: '))
    celsius = (farenheit - 32) * 5/9
    print(f'A temperatura em Celsius é: {celsius:.2f}')
else:
    print('Opção inválida!')