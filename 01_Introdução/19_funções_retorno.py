# Com retorno
# com mais de 1 retorno
# Desafio de aula: Cara ou Coroa

# Função diz oi

def diz_oi(): #para criar a funcao necessariamente precisa de () e :
    return 'Oi'

# Função canta parabéns

def cantar_parabens(): 
    return 'Parabéns para você!'

# Função soma 2 valores

def soma():
    a = 10
    b = 18
    return a + b #return é um break para a função

#print(soma() * 10) 

#desafio cara ou coroa: 

from random import random, randint
# print(random()) #entre 0 e 1
# print(randint(1, 10)) #entre 1 e 10

def teste():
    dado =1
    if dado >= 5:
        return 'É maior!'
    return 'É menor!'




def cara_coroa(): 
   if random() >= 0.5:
       return 'Cara'
   return 'Coroa'

print(cara_coroa()) 