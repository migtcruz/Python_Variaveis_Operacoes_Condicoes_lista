preco = float(input('Digite o valor do produto > R$ '))
desc = preco * 0.05
print('Valor do produto R${} \nValor do desconto R$ {:.2f} \nValor total R$ {:.2f}'.format(preco, desc, (preco-desc)))
