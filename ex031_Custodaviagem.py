dist = float(input('Qual a distancia em hm: '))
if dist <= 200:
    v1 = dist * 0.50
    print('Distancia: {} km >> Valor da Viagem: RS {:.2f}'.format(dist, v1))
else:
    v2 = dist * 0.45
    print('Distancia: {} km >> Valor da Viagem: R$ {:.2f}'.format(dist, v2))
    
