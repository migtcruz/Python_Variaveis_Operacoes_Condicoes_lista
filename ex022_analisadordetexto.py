nome = str(input('Digite seu nome completo: ')).strip()
'''strip elimina os espacos antes e depois'''
print('Letras Maisculas: {}'.format(nome.upper()))
print('Letras Minusculas: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(" ")))
print('Seu 1º nome tem {} letras'.format(nome.find(' ')))

