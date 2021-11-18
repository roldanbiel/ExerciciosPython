
preco = float(input('Digite o preço do produto: '))
valor_desc = int(input('Informe o desconto: '))

desconto = valor_desc / 100
valor_final = preco - (preco * desconto)

print('Valor total do produto sem desconto é de R${}.'.format(preco))
print('Valor do produto com desconto é de R${}.'.format(valor_final))
