#caixa eletrônico
def linha():
	print('*'*30)

linha()
print('Banco x³')
print('caixa eletronico')
def menu():
	print('''________€€_______
1. Saldo em tela
2. Saque
3. Pagar fatura com saldo
4. Transfência via Pix
''')
menu()
valor_fatura = 2563.75
saldo = 234567.03


escolha = int(input('Digite O serviço desejado: '))

match escolha:
	case 1:
		print(f'Seu saldo é R$: {saldo}')
		voltar = input('Deseja retornar ao menu anterior? S/N ')
		voltar = voltar.capitalize()
		if voltar == 'S':
			menu
			escolha = int(input('Digite O serviço desejado: '))
		else:
			print('obrigado por usar nossos serviços!')	
	case 2:	
		numero = int(input('Digite o valor que deseja sacar: '))
		if numero <= saldo and numero >= numero:
			print('Contando cedulas')

			cem = int(numero / 100)
			numero = numero % 100
	
			cinquenta = int(numero/50)
			numero = numero % 50
	
			dez = int(numero/10)
			numero = numero % 10
	
			cinco = int(numero/5)
			numero = numero % 5

			um = numero 

			print('Notas R$100,00 = ',cem)
			print('Notas R$ 50,00 = ',cinquenta)
			print('Notas R$ 10,00 = ',dez)
			print('Notas R$  5,00 = ',cinco)
			print('Notas R$  1,00 = ',um)
	
			
		else:
			print('Saldo insuficiente')
	case 3:
		print(f'O valor total da fatura é R$: {valor_fatura}.')
		valor = input('Deseja pagar o valor total? S/N ')
		valor =valor.capitalize()
		if valor =='S':
			decisao = input(f'Posso confirmar o pagamento de R$: {valor_fatura} do seu saldo? S/N ')
			decisao = decisao.capitalize()
			if decisao =='S':
				if saldo >= valor_fatura:
					fatura_paga = saldo-valor_fatura
					print(f'Operação realizada com sucesso.')
					saldo = fatura_paga
					print(f'Seu novo saldo é R$: {saldo}')
				else:
					pass	
			else:
				pass
		else:
			pass	
	case 4:
		transferencia = float(input('Qual o valor que deseja transeferir: '))
		def men():
			print('''
			Escolha uma chave pix:
			1- CPF
			2- CNPJ
			3- TELEFONE
			4- E-MAIL
			5- ALEATÓRIA
			''')
		men()
		chave = int(input('Digite uma opção: '))	
		match chave:
			case 1:
				cpfbd = 00000000000
				cpf = int(input('Digite os numeros do cpf sem ponto ou traço:'))
				if cpf == cpfbd:
					saldo >= transferencia
					confirm = input('confirmar transferencia? S/N ')
					confirm = confirm.capitalize()
					saldo = saldo-transferencia
					print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
					
				elif cpf != cpfbd:
					print('Humm!! Você digitou algum dado errado. ')
					men()
					chave = int(input('Digite uma opção: '))
					match chave:
						case 1:
							cpfbd = 00000000000
							cpf = int(input('Digite os numeros do cpf sem ponto ou traço:'))
							if cpf == cpfbd:
								saldo >= transferencia
								confirm = input('confirmar transferencia? S/N ')
								confirm = confirm.capitalize()
								saldo = saldo-transferencia
								print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
							else:
								print('Programa encerrado')
			case 2:
				cnpjbd = 00000000000000
				cnpj = int(input('Digite os numeros do cnpj sem ponto ou traço:'))
				if cnpj == cnpjbd:
					saldo >= transferencia
					confirm = input('confirmar transferencia? S/N ')
					confirm = confirm.capitalize()
					saldo = saldo-transferencia
					print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
					
				elif cnpj != cnpjbd:
					print('Humm!! Você digitou algum dado errado. ')
					men()
					chave = int(input('Digite uma opção: '))
					match chave:
						case 1:
							cnpjbd = 00000000000
							cnpj = int(input('Digite os numeros do cpf sem ponto ou traço:'))
							if cnpj == cnpjbd:
								saldo >= transferencia
								confirm = input('confirmar transferencia? S/N ')
								confirm = confirm.capitalize()
								saldo = saldo-transferencia
								print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
							else:
								print('Programa encerrado')	
			case 3:	
				telefonebd = 0000000000
				telefone = int(input('Digite os numeros do telefone:'))
				if telefone == telefonebd:
					saldo >= transferencia
					confirm = input('confirmar transferencia? S/N ')
					confirm = confirm.capitalize()
					saldo = saldo-transferencia
					print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
					
				elif telefone != telefonebd:
					print('Humm!! Você digitou algum dado errado. ')
					men()
					chave = int(input('Digite uma opção: '))
					match chave:
						case 1:
							telefonebd = 00000000000
							telefone = int(input('Digite os numeros do telefone:'))
							if telefone == telefonebd:
								saldo >= transferencia
								confirm = input('confirmar transferencia? S/N ')
								confirm = confirm.capitalize()
								saldo = saldo-transferencia
								print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
							else:
								print('Programa encerrado')									
			case 4:
				emailbd = fulano.ciclano@abc.com.br
				email = input('Digite os numeros do telefone:')
				if email == emailbd:
					saldo >= transferencia
					confirm = input('confirmar transferencia? S/N ')
					confirm = confirm.capitalize()
					saldo = saldo-transferencia
					print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
					
				elif email != emailbd:
					print('Humm!! Você digitou algum dado errado. ')
					men()
					chave = int(input('Digite uma opção: '))
					match chave:
						case 1:
							emailbd = fulano.ciclano@abc.com.br
							email = int(input('Digite o email:'))
							if email == emailbd:
								saldo >= transferencia
								confirm = input('confirmar transferencia? S/N ')
								confirm = confirm.capitalize()
								saldo = saldo-transferencia
								print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
							else:
								print('Programa encerrado')	
			case 5:
				aleatoriabd = ('qwerty123asdf456zxcv789')
				aleatoria = input('Digite os numeros da chave aleatoria:')
				if aleatoria == aleatoriabd:
					saldo >= transferencia
					confirm = input('confirmar transferencia? S/N ')
					confirm = confirm.capitalize()
					saldo = saldo-transferencia
					print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
					
				elif aleatoria != aleatoriabd:
					print('Humm!! Você digitou algum dado errado. ')
					men()
					chave = int(input('Digite uma opção: '))
					match chave:
						case 1:
							aleatoriabd = 'qwerty123asdf456zxcv789'
							aleatoria = int(input('Digite os numeros da chave aleatoria:'))
							if aleatoria == aleatoriabd:
								saldo >= transferencia
								confirm = input('confirmar transferencia? S/N ')
								confirm = confirm.capitalize()
								saldo = saldo-transferencia
								print(f'Transferencia realizada com sucesso. Seu novo saldo é R$: {saldo}')
							else:
								print('Programa encerrado')					
