
preco = float(input('Digite o valor total das compras: '))

print('''FORMAS DE PAGAMENTO
[1] - À VISTA (DINHEIRO/CHEQUE)
[2] - À VISTA (CARTÃO)
[3] - 2X NO CARTÃO
[4] - 3X OU MAIS NO CARTÃO (MAX. de 12X)''')
opcao = int(input('Qual é a opção? '))
print('Opção {} selecionada.'.format(opcao))

if opcao == 1:
    desconto = preco - (preco * 0.1)
    desc = preco * 0.1
    print('Valor total da compra será de R${:.2f}.'.format(desconto))
    print('Valor à vista no dinheiro tem 10% de desconto.')
    print('Seu desconto foi de R${}.'.format(desc))
    print('Muito obrigado pela preferência!')
elif opcao == 2:
    desconto = preco - (preco * 0.05)
    desc = preco * 0.05
    print('Valor total da compra será de R${:.2f}'.format(desconto))
    print('Valor à vista no cartão tem 5% de desconto.')
    print('Seu desconto foi de R${}.'.format(desc))
    print('Muito obrigado pela preferência!')
elif opcao == 3:
    parcela = preco / 2
    print('Pagamento em 2x.')
    print('Valor total da compra: R${:.2f}.'.format(preco))
    print('Valor da parcela: R${}.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    qtd = int(input('Quantidade de parcelas: '))
    parcela = total / qtd
    print('Valor total da compra: R${:.2f} com juros.'.format(total))
    print('Valor da parcela: R${}.'.format(parcela))
else:
    print('\033[1;31mOpção inválida\033[m')
