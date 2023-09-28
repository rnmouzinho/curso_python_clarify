# # Sets

# tupla1: ()
# tupla2 = tuple()

# lista1 = []


# conjunto 1 = {'Ricardo', 10, 20}
# conjunto2 = set()

# numeros = {6, 5, 8, 3, 'Ricardo', 20}

# Analise cidades (cada pessoa que entrou colocou a cidade de nascimento)
cidade = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina',
          'Salvador','Juiz de Fora', 'Rio de Janeiro', 'Petrolina',
          'Salvador', 'São Paulo', 'São Paulo', 'São Paulo',  'Juiz de Fora',
          'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador',
          'Juiz de Fora',  'Petrolina', 'Salvador', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo',
          'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro',  'São Paulo', 'Rio de Janeiro',
          'São Paulo', 'Rio de Janeiro', 'São Paulo']


# quantas pessoas vieram? (total)
#print(cidade) #mostra todo conjunto 
#print(f'Total de Pessoas: {len(cidade)}')


# quantas pessoas passaram são do Rio?
# print(f'Total de Pessoas do RJ: {cidade.count("Rio de Janeiro")}') #se ja comecou com aspas simples dentro precisa de dupla

# #quais cidades recebi aluno? 

# print(f'Quantidade de cidades: {len(set(cidade))}')
# print(f'Cidades: {set(cidade)}')

curso_python = {'Ricardo', 'Ric', 'Ri', 'R', 'Nunes', 'Nun'}
curso_sql = {'Ricardo', 'Ric', 'Ri', 'Ricard', 'Nunes', 'Nun'}

#total de alunos: 

print(f'QTD alunos PY: {len(curso_python)}')
print(f'QTD alunos SQL: {len(curso_python)}')

total_alunos1 = curso_python.union(curso_sql) #gera uma lista unica sem repetições (contagem distinta)
total_alunos2 = curso_python | curso_sql 

print(f'Total de alunos: {len(total_alunos1)}')

#alunos nos 2 cursos

ambos_curso1 = curso_python.intersection(curso_sql)
ambos_curso2 = curso_python & curso_sql

print(f'Alunos nos 2 cursos: {len(ambos_curso2)}')

#alunos matriculados em apenas um curso: 

so_python = curso_python.difference(curso_sql)
so_python2 = curso_python - curso_sql
so_sql = curso_sql.difference(curso_python) 

print(so_python)
print(f'Só Python: {len(so_python)}')
print(so_sql)
print(f'Só SQL: {len(so_sql)}')
print(so_python2)