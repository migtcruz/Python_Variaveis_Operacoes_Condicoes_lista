sal = float(input('Digite o salario do funcionario > R$ '))
aum = sal * 0.15
total = aum + sal
print('Salario R${} \nValor 15% aumento R${:.2f} \nNovo Salario R${:.2f}'.format(sal, aum, total))