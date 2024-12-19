nome = str(input('Digite seu nome completo: ')).strip().upper()
n = nome.split()
print('Ola, muito prazer...')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1]))

