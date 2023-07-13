from funcoes_banco import *

print('Bem - Vindo ao seu banco!')
print()
clientes = []
dados = {}

while True:
    menu()
    acao = int(input())
    print()

    # Cadastro
    cont = 0 
    if acao == 0:
        cont = 0
        dados = {}
        while cont != 'N':
            print('Faça seu cadastro!')
            print()
            armazenar()   
            print('Se desejar cadastrar novo cliente digite [S], se não digite [N].')
            print()
            cont = input().upper()
            print()
        
    # Verificar saldo
    if acao == 1:
       verificar_saldo()       
    
    # Depositar dinheiro
    if acao == 2:
        depositar()
   
    # Sacar dinheiro
    if acao == 3:
        sacar()
   
    # Encerrar o atendimento
    if acao == 4:
        encerrar()
        break