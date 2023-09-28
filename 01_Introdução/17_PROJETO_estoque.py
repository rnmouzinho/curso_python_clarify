"""
Cadastre 3 produtos no estoque, cada produto precisa ter:
- nome
- preço
- data e hora que foi cadastrado
- Nome do Funcionário

Em seguida, permita que os produtos sejam visualizados.
"""
from datetime import datetime
estoque = []

while True:
    menu = int(input('1| Cadastrar\n2| Visualizar\n3| Sair\nOpcão: '))

    match menu:
        case 1: #cadastrar produto
            produto = dict(
                nome_produto = str(input('Nome: ')).title(), 
                preco = float(input('Preço: R$ ')), 
                nome_funcionario = str(input('Funcionário: ')).title(),
                dt_cadastro = datetime.now().strftime('%d.%m.%Y | %H:%M')
            )
            estoque.append(produto)

        case 2: #visualizar estoque
            for i, p in enumerate(estoque):
                print(f'\nProduto: {i+1}')
                for c, v in p.items():
                    print(f'{c} → {v}')
                print() #só para pular uma linha

        case 3: #sair
            break
        
        case _:
            print('Opção Inválida')