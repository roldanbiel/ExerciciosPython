from math import hypot

# Maneira sem 'import math'
cateto_op = float(input('Valor do cateto oposto: '))
cateto_ad = float(input('Valor do cateto adjacente: '))

hipotenusa = (cateto_op ** 2 + cateto_ad ** 2) ** 0.5

print('Hipotenusa vale {:.2f}.'.format(hipotenusa))

# Maneira com 'import math'

cateto_op = float(input('Valor do cateto oposto: '))
cateto_ad = float(input('Valor do cateto adjacente: '))

hi = hypot(cateto_op, cateto_ad)
print('Hipotenusa vale {:.2f}.'.format(hi))
