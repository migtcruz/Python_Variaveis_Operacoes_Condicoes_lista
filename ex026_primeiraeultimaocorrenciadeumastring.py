frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A apareceu {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))

