"""
Primeiro passo para leitura, é abrir o arquivo, para isto usamos
a função OPEN(nomeArquivo).
O parâmetro é o nome ou caminho do arquivo.

O arquivo deve existir, caso contrário retornará erro FileNotFound.

Open apenas abre o arquivo, para ler seu conteúdo é necessário usarmos
a função nomeArquivo.read()
Por padrão o Open abre com o parâmetro r(read)
"""

# criando um arquivo txt

#with open('./base/teste.txt', 'a', encoding='utf8') as arquivo: #cria o arquivo caso nao exista se ele existir insere info dentro do arquivo
    #arquivo.write('\nSó um teste') #o \n serve para nao escrever na mesma linha

# a -> adc w -> sub r -> leitura (pode ser suprimido)

# with open('./base/teste.txt', 'w', encoding='utf8') as arquivo:
#     arquivo.write('\nSó um teste') 

#with open('./base/teste.txt', 'r', encoding='utf8') as arquivo: #cria o arquivo caso nao exista se ele existir insere info dentro do arquivo
   #print(arquivo.read()) 


# tratamento de erro

# try: 
#     with open('comando Git Ricardo.txt', 'r', encoding='utf8') as arquivo:
#         texto = arquivo.read()

# except FileNotFoundError: #nao exibe tela de erro para o usuário e sim uma mensagem e nao fecha o programa/app
#     print('Arquivo não encontrado')

# finally: #sempre é executado, pode ser uma mensagem final por ex
#     print('Volte Sempre!')

# # Exercício de aula: criar um todo (lista de tarefas)

def to_do():
    while True:
        try:
            menu = int(input('1| Inserir\n2| Visualizar\n3| Sair\nOpção: '))
        except ValueError:
            print('Opção Inválida')

        match menu:
            case 1:
                try: 
                    with open('./base/to_do.txt', 'a', encoding='utf8') as arquivo:
                        while True:
                            tarefa = str(input('Digite uma Tarefa ou S para Sair: '))
                            if tarefa.lower() != 's':
                                arquivo.write(f'{tarefa}\n')
                            else:
                                break
                except FileNotFoundError: 
                    print('Arquivo não encontrado')

            case 2:
                try:
                    with open('./base/to_do.txt', 'r', encoding='utf8') as arquivo:
                        print(arquivo.read())
                except FileNotFoundError:
                        print('Arquivo não encontrado')

            case 3:
                break

            case _: 
                print('Opção inválida')

to_do() 
