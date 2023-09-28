"""
Vamos iniciar um programa que receba:
 nome = str(input('Digite seu nome)).title()
 idade
 peso
 altura

Retorne o IMC do usuário.

IMC =   Peso
      --------
       Altura²
"""

nome = str(input('Digite seu nome: ')).title()
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = (peso/altura**2)

print(f'{nome}, Seu IMC é: {round(imc,2)}')





