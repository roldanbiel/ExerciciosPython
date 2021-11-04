"""
Escreva um programa que ajude vendedores. A partir de um valor total lido, mostre:

- o total a pagar com 10% de desconto;
- o valor de cada parcela, no parcelamento de 3x sem juros;
- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
- a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

valor_produto = float(input('Valor total do produto: '))

desconto_bruto = valor_produto * 0.1
produto_desconto = valor_produto - desconto_bruto
parcela = valor_produto / 3
comissao1 = produto_desconto * 0.05
comissao2 = valor_produto * 0.05


print('Valor do produto com 10% de desconto é de:', 'R$', produto_desconto, 'reais.')
print('Valor da parcela do produto (3x):', 'R$', parcela, 'reais.')
print('Sua comissão de venda a vista será de:', 'R$', comissao1, 'reais.')
print('Sua comissão de venda parcelada será de:', 'R$', comissao2, 'reais.')
