"""
Estrutura condicionais mais utilizada em menus,
funciona semelhante ao escolhaCaso do portugol
e switch case no java por exemplo...
"""
# Calculadora

''' 
Conclua o exemplo inserindo: 
    multiplicar, dividir e resto da divisão.
'''

menu = int(input('[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAR\n[4]DIVIDIR\nOpção: '))

if menu >=1 and menu <=4:
    valor1 = float(input('Digite o Valor 1: '))
    valor2 = float(input('Digite o Valor 2: '))

match menu:
    case 1:
        print('Somando...aguarde')
        print(valor1 + valor2)
    case 2:
        print('Subtraindo...aguarde')
        print(valor1 - valor2)
    case 3:
        print('Multiplicando...aguarde')
        print(valor1 * valor2)
    case 4:
        print('Dividindo...aguarde')
        print(valor1 / valor2)
    case _:
        print('Erro, opção inválida! Tente Novamente')