"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> inicio, fim, passo
* Enumerate -> Permite acesso ao índice
"""

# sintaxe


'''
Desafio de aula: Crie um sistema que receba 4 notas 
e calcule a média, ao fim apresente a média e situção
do aluno, sendo:
>7 aprovado, >5 em recuperação e <5 reprovado.
'''
# nota1 = float(input('Digite a 1ª Nota: '))
# nota2 = float(input('Digite a 1ª Nota: '))
# nota3 = float(input('Digite a 1ª Nota: '))
# nota4 = float(input('Digite a 1ª Nota: '))

# media = (nota1 + nota2 +nota3 +nota4) / 4

notas = 0
for contador in range(1, 5):
    nota = float(input(f'Digite a {contador}º Nota: '))
    if nota >=0 and nota <=10:
        notas = notas + nota 
    else:
        print ('Nota Inválida')

media = notas / contador 

if (media >=7.0 and media <=10.0):
    print('Aluno Aprovado!')
elif (media >= 5.0 and media < 7.0):
    print('Aluno em Recuperação')
elif (media >0.0 and media <= 5.0):
    print('Aluno em Recuperação')
else:
    print('Nota Inválida')




