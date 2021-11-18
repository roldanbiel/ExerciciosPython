import math

angulo = float(input('Informe o ângulo: '))

cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('COSSENO de {} é {:.2f}'.format(angulo, cos))
print('SENO de {} é de {:.2f}'.format(angulo, sen))
print('TANGENTE de {} é de {:.2f}'.format(angulo, tan))
