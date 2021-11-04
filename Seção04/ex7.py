"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Clesius.
A fórmula da conversão é: F = C*(9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e
C a temperatura em Celsius.

"""

temperatura = float(input('Informe a temperatura em Graus Fahrenheit: '))

c = 5.0 * (temperatura - 32.0) / 9

print(c)
