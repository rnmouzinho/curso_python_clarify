"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

* SORT >>> Ordena os dados de uma lista.
* REVERSE >>> Inverte a lista.
* APPENDD >>> Atribui a lista, um elemento por vez. Podendo ser inclusive outra lista...
* INSERT >>> Atribui vários elementos, integrando à lista original.
* POP >>> Remove um valor da lista por índice.
* REMOVE >>> Remove um valor da lista por valor.
* ENUMERATE >>> Acesso à chave e valor.
* SHALLOW COPY
* CLEAR >>> Limpa a lista.
"""

# lista1 = []
# lista2 = list()

# n10 = [range(0, 101, 10)]
# n10_2= list(range(0,120, 10))


# print(n10_2) 

#notas = []

for n in range(4):
    notas.append(float(input('Nota: ')))

# notas.sort() #orderna a lista
# notas.reverse() #inverte a ordem
# print(notas)

notas = [8, 5, 2, 10]
print(notas)
notas.pop(2) #exclui o valor da posicao em ()
notas.remove(8) #procura e exclui o valor exato(item) e não a posição
print(notas) 
notas.append(4) #adiciona o valor na ultima posicao
notas.insert(1, 15) #adiciona o valor "15" na posição indicada "1" 

