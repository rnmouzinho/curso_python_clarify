"""
While >>> Utilizada quando se sabe a quantidade de repetições e
quando não se sabe.
* Necessário atentar para o critério de parada.

Sintaxe >>>  while expressão_bool:
                    Execução.

Expressão será executada enquanto for verdadeira.
Expressão Booleana >>> Toda expressão onde o resultado
for Verdadeiro ou Falso.

Ex.
resposta = ''
    while resposta != 'SIM':
            resposta = 'input'
"""

# for cont in range(5)
#     print('Batata')

# numero = 0 #precisa começar com um número
# while numero <5: 
#     print('Frita')
#     numero += 1




# repetindo um texto 5 vezes com for
# repetindo um texto 5 vezes com while
# validando uma senha de forma simples

#senha_cadastrada = str(input('Cadastre sua Senha: ')).lower()
#senha = ''

#while senha != senha_cadastrada: 
    #senha = str(input('Digite sua senha para entrar: ')).lower()
    #if senha != senha_cadastrada:
        #print('Senha Incorreta!!')

#print('Acesso Autorizado!!')

qtd_notas = 1 
soma_notas = 0
while qtd_notas <= 4: 
    nota = float(input(f'Digite a {qtd_notas}ª nota: '))
    if nota >= 0 and nota <=10:
        qtd_notas +=1 
        soma_notas += nota
    else:
        print('Tente Novamente. Nota Inválida')

média = round(soma_notas / qtd_notas, 1)
print(f'Média: {média}')

