vel = float(input('Digite a velocidade do carro em km/h: '))

if vel > 80.0:
    print('MULTADO !! Voce excedeu o limite de 80 Km/h')
    multa = (vel - 80) * 7
    print('Valor Multa: R$ {:.2f} '.format(multa))
else:
    print('Sua vel é de {} dentro do limite de 80 Km/h'.format(vel))
