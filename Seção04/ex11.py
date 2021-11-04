"""
Leia uma velocidade em m/s e apresente-a convertida em km/h.
A fórmula de conversão é: K = M * 3.6, sendo K a velocidade em km/h e
M a velocidade em m/s.
"""

velocidade = float(input('Digite uma velocidade em m/s (metros por segundo): '))

km = velocidade * 3.6

print(km)
