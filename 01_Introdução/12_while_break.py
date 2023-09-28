"""
While com Break
while True: >>> este laço será executado enquanto 
não encontrar o Break pelo caminho.
Break >>> Condição de parada de um loop. (FLAG)
"""
# sintaxe
# Validando tipo de dado com break

# qtd_notas = 0 # OU unindo em uma linha: qtd_notas = soma_notas = 0 
# soma_notas = 0
# while True: 
#     nota = float(input(f'Digite a {qtd_notas+1}ª nota: '))
#     if nota >= 0 and nota <=10:
#         qtd_notas +=1 
#         soma_notas += nota
#     else:
#         print('Tente Novamente. Nota Inválida')

#     if qtd_notas ==4:
#         break

# média = round(soma_notas / qtd_notas, 1)
# print(f'Média: {média}')

while True:
    menu = int(input('[1] SOMAR\n[2]SUBTRAIR\n[3]SAIR\nOpção: '))
    if menu ==1 or menu ==2:
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
            print('Fechando Aplicativo...')
            break
        case _:
            print('Erro, opção inválida! Tente Novamente...\n') 
