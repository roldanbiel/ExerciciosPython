"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula da conversão é: F = C*(9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e
C a temperatura em Celsius.
"""

temperatura = float(input('Informe a temperatura em Graus Celsius: '))

f = temperatura * (9.0 / 5.0) + 32

print(f)
