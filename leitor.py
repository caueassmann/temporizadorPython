from Jsonclass import JsonClass

ACCEPTED 				= ["read all", "search", "close"]
ACCEPTED_SEARCH 		= ["last","first"]
ACCEPTED_READ_ALL 		= ["Tarefa","dia","hora","pagamento","tempo","todos"]

ARQUIVOJSON = "logs.json"

print("Leitor do arquivo logs.json: ")
print("---------------------------")
print("Comando aceitos:")
print(ACCEPTED)

close = False

while close == False:
	entrada = input("Digite o comando: ")

	if(entrada in ACCEPTED):
		jman = JsonClass()
		leitura = jman.lerJson(ARQUIVOJSON)
		if(entrada == "read all"):
			laco = True

			while laco:
				print("Leitura total selecionada...")
				print("----------------------------")
				print("Comando Aceitos: ")
				print(ACCEPTED_READ_ALL)
				
				entrada_read = input("Digite um comando: ")
				if(entrada_read in ACCEPTED_READ_ALL):
					laco = False
					if(entrada_read == "todos"):
						for dado in leitura:
							print(dado["Tarefa"])			
					else:
						for dado in leitura:
							print(dado[entrada_read])
							
				else:
					print("------------")
					print("Comando Não encontrado")


		elif(entrada == "search"):
			laco = True
			while laco:
				print("Pesquisa Selecionada...")
				print("Comandos aceitos: ")
				print(ACCEPTED_SEARCH)

				entrada_search = input("Digite um comando: ")
				if(entrada_search in ACCEPTED_SEARCH):
					laco = False
					integers = int(input("Número de registros: "))
					if(type(integers) != int):
						integers = 15
						print("Valor inválido, definido 15 como padrão")
					leitura = leitura[: integers]
					
					if(entrada_search == "last"):
						leitura = reversed(leitura)
					
					for dado in leitura:
						print(dado)
				else:
					print("------------")
					print("Comando Não encontrado")
		
		elif(entrada == "close"):
			exit()
	else:
		print("------------")
		print("Comando Não encontrado")

