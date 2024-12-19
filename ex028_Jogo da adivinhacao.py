from random import randint
from time import sleep
cpu = randint(0, 5)
print('-*-' * 20)
print("Vou pensar em um num entre 0 e 5. Tente adivinhar !!!!")
print('-*-'*20)
jog = int(input('Digite um numero entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if jog == cpu:
    print('PARABENS!! VC ACERTOU...')
else:
    print('VC ERROU !! o numero que pensei: {} e o numero que vc pensou: {}'.format(cpu, jog))
