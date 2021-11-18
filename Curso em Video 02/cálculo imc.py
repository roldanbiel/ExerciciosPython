print('\033[1;33m---\033[m'*9)
print('\033[1;33mCálculo do IMC (Peso Ideal)\033[m')
print('\033[1;33m---\033[m'*9)
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('\033[1;33mVocê está abaixo do peso ideal. Vamos melhorar isso ai!\033[m')
elif 18.5 <= imc < 25:
    print('\033[1;32mParabéns, você está no peso ideal.\033[m')
elif 25 <= imc < 30:
    print('\033[1;33mVocê está com excesso de peso. Vamos trabalhar mais!\033[m')
elif 30 <= imc < 40:
    print('\033[1;31mCuidado! Você está na obesidade. Cuide da sua saúde!\033[m')
elif imc >= 40:
    print('\033[1;31mVá urgente em algum médico. Você está com obesidade mórbida.\033[m')
