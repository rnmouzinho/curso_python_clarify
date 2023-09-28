"""
Python possui o que chamamos de tipagem fraca.

STRING por padrão, sempre estará entre
    ' ' aspas simples
    " " aspas duplas
    ''' ''' aspas simples triplas
    E aspas duplas trilas, como esta que cerca este comentário.
"""
# Fatiamento de String
# Metodos (podem ser utilizados na mesma construção.)
# Número inteiro - int | ex: 123 65 98 90
# Float >>> Números reais/ decimais separados por . e não ,
# correto
# errado
# Booleano >>> 2 constantes - Verdadeiro (True) e falso (false).

#nome = str(input('Digite seu nome: ')).title() #ajusta o texto

dado = '     RiCARdo MouZINHo'

print(dado)
print(dado.title()) # 1ª letra maiúscula de cada palavra
print(dado.upper()) # letras maiúsculas
print(dado.lower()) # letras minúsculas
print(dado.capitalize()) # 1ª maiúscula só da 1ª palavra

print(len(dado)) #conta caracteres
print(len(dado.strip())) #limpa caracteres desnecessários mas apenas do iniicio ou do final e nao no meio


#Inteiro
numero = 10
print(numero * 100)
idade = int(input('Idade: '))
#Float 
altura = 1.83
alt= float(input('Altura: '))
#Booleano Bolean Bool 
status = True
status = False 
print('a' in 'Ricardo')
