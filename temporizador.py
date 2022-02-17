from datetime import datetime, timedelta, date
from sys import stdout, stdin
from time import sleep
from NonBlockingConsole import NonBlockingConsole
from Jsonclass import JsonClass

ARQUIVOJSON = 'logs.json'
PAGAMENTOHORA = 9

jman = JsonClass()
arquivo = jman.lerJson("logs.json")
tarefa = input("Qual a tarefa que irá desempenhar? ")	
data = datetime.now()
data_text = '{}/{}/{}'.format(data.day, data.month,data.year)
hora_text = '{}:{}'.format(data.hour,data.minute)
with NonBlockingConsole() as nbc:
	print(' Cronometro progressivo')
	tempo = timedelta()
	print('\n')
	x = True
	while (x):
		if nbc.get_data() == '\x1b':
			break
		stdout.write("\r%s   === Pressione ESC para finalizar: "%tempo)
		stdout.flush()
		tempo = tempo + timedelta(seconds=1)
		sleep(1)
		
	minutos = (tempo.total_seconds())/60
	pagamento = round((PAGAMENTOHORA/60)*minutos,2)
	
	dataJson = {
	"Tarefa" : f"{tarefa}",
	"dia" : f"{data_text}",
	"hora" : f"{hora_text}",
	"tempo" : f"{minutos}",
	"pagamento" : f"{pagamento}"
	}

	arquivo.append(dataJson)
	jman.gravarJson(ARQUIVOJSON,arquivo)