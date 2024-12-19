import random
n1 = str(input('Digite nome 1 : '))
n2 = str(input('Digite nome 2 : '))
n3 = str(input('Digite nome 3 : '))
n4 = str(input('Digite nome 4 : '))
lista = [n1, n2, n3, n4]
escolha = random.choice(lista)
print('O nome escolhido é : {}'.format(escolha))

