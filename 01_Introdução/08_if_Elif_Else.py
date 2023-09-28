"""
IF, ELSE, ELIF
Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Sintaxe:

if (teste):
    Bloco que será executado se o teste retornar True
"""

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''

# nota = 6.5

# if nota >=7:
#     print('Aluno Aprovado') #o else só funciona quando der falso o teste (if)

# else: 
#     print('Aluno Reprovado')
    


# Condição simples
# Condição composta
#nota = float(input('Nota: ')

# if (nota >= 5 and nota < 7):
#     print('Aluno em Recuperação')

# elif (nota >= 7 and nota <= 10):
#     print('Aluno Aprovado')

# elif (nota >= 0 and nota < 5):
#     print('Aluno Reprovado')

# else:
#     print('Formato da Nota Inválida')

# Condição aninhada
''' Vamos criar um sistema para validadar se o cliente
pode ou não ter uma Habilitação de acordo com a idade 
que irá informar.
'''

idade = int(input('Digite a sua idade: '))

if (idade >=18 and idade <=130):
    print('Autorizado')
elif (idade >=16 and idade <18):
    resp = str(input('Possui autorização (sim|não?)')).lower()
if (resp == 'sim'):
    print('Autorizado')
elif (resp == 'não' or resp == 'nao'):
    print('Não autorizado')
elif (idade >=0 and idade <16):
    print('Não autorizado')
else:
    print('Idade Inválida')




# Operadores unitários >>> Dependem de um único valor >>> not, is
# Operadores binários >>> Dependem de mais que 1 valor >>> and, or



