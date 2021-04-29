import sys
import csv

#Passos do software


def abrir_csv(arquivo):
	with open(arquivo, mode='r', encoding='utf-8') as arquivo:
		dados= csv.DictReader(arquivo, delimiter=';')
		return list(dados)


def procurar_dados(bd, valor, pesquisa, retorno):
	print(bd)
	for dado in bd:
		if dado[pesquisa]  == valor:
			return dado[retorno]
	return False


def main():
	###
	#1) Coletar código do totem
	serial=input('Digite o serial do totem: ')
	bd=abrir_csv('tabela.csv')
	loja=procurar_dados(bd, serial, 'Serial','IP')
	print (loja)
	
	#2) Verificar se já existe configuração salva deste totem
	#3) Caso sim, resgatar as configurações
	#4) Caso não, gerar novas configurações e gravar
	#5) Salvar os arquivos de configurações do software.
	###

if __name__ == '__main__':
	sys.exit(main())
