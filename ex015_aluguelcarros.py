dias = int(input('Informe a quantidade de dias: '))
km = float(input('Informe a quantidade de Km rodados: '))
vdias = dias * 60
vkm = km * 0.15
print('Total de dias {} Total de Km rodados {} Valor a pagar R$ {:.2f}'.format(dias, km, (vdias+vkm)))

