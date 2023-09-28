"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:
______________________________________________
| Menor que 18.5      | Abaixo do peso       |
| Entre 18.5 - 24.9   | Peso Normal          |
| Entre 25.0 - 29.9   | Excesso de peso      |
| Entre 30.0 - 34.9   | Obesidade classe I   |
| Entre 35.0 - 39.9   | Obesidade classe II  |
| Maior ou igual 40.0 | Obesidade classe III |
----------------------------------------------

Mostre também a data deste resultado.
"""

nome = str(input('Digite seu nome: ')).title()
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = (peso/altura**2)
print(f'O seu imc é: {round(imc,2)}')

if (imc <18.5):
    print('Abaixo do Peso')
elif (imc >= 18.5 and imc < 25.0):
    print('Peso Normal')
elif (imc >= 25.0 and imc < 30.0):
    print('Excesso de Peso')
elif (imc >= 30.0 and imc < 35.0):
    print('Obesidade I')
elif (imc >= 35.0 and imc < 40.0):
    print('Obesidade II')
elif (imc >= 40.0):
    print('Obesidade III')

from datetime import datetime

print(datetime.now().strftime('%d | %m | %Y %H:%M'))









