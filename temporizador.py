from datetime import datetime, timedelta, date
from sys import stdout, stdin
from time import sleep
from NonBlockingConsole import NonBlockingConsole

PAGAMENTOHORA = 9
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
	string = "Tempo empenhado fazendo a tarefa {}, no dia {}, ás {}: {}. Pagamento total: R$ {} \n".format(tarefa, data_text, hora_text, tempo,pagamento)
	arquivo= open("logs.txt","a")
	arquivo.write(string)
	arquivo.close()