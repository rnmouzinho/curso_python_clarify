"""
 Faça um programa que leia ano de nascimento de 5 pessoas e no final
 mostre quantas pessoas já atingiram a maioridade e para aquelas que
 ainda atingiram, mostre a média em anos que faltam para chegarem a maior idade.
"""



from datetime import date

ano_atual = date.today().year
qtd_maior = qtd_menor = soma_menor = 0

for cont in range(5):
    ano_nasc = int(input('Digite o ano de Nascimento: '))

    if (ano_atual - ano_nasc) >= 18:
        qtd_maior +=1
        print ('Maior de idade identificado!\n')
    
    else:
        qtd_menor += 1
        soma_menor += 18 - (ano_atual- ano_nasc)
        print('Menor de Idade Identificado...\n')

media = soma_menor / qtd_menor