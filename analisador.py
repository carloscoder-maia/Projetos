print('Analisador de nomes')

nome = input('Digite seu nome completo: ')
print(f'Seu nome em maiúsculas é : {nome.upper()}')
print(f'Seu nome em minúsculas é : {nome.lower()}')
print(f'Seu nome tem {len(nome.strip())} letras')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')