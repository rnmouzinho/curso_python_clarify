import time
from datetime import datetime
from pytz import timezone

# utilizando a Lib TIME

#print(time.localtime()) todos os dados
print(time.localtime().tm_year) #dados específicos

# utilizando a Lib DATETIME

print(datetime.today())
print(datetime.now().date())
print(datetime.now().time())

# utilizando a Lib PYTZ

dthr = datetime.now()
fuso_br = timezone('America/Sao_Paulo')
sp = dthr.astimezone(fuso_br)
sp_corrigido = sp.strftime('%d-%m-%Y | %H:%M') #função que ajusta a formatação da data e hora

print(sp)
print(sp_corrigido)


