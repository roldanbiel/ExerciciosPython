"""
Uma empresa contrata um encanador a R$30 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá
ser paga, sabendo-se que são descontados 8% de imposto de renda.
"""

pagamento = 0
pag_final = 0
imposto = 0

numero_dias = int(input('Informe o número de dias trabalhos pelo encanador: '))

pagamento = 30 * numero_dias
imposto = pagamento * 0.08

pag_final = pagamento - imposto

print(pag_final)
