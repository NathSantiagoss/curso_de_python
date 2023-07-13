print('Bem - Vindo ao seu banco!')
clientes = []


while True:
    print("Digite qual ação você quer fazer:\n\
    [0] Criar conta\n\
    [1] Verificar saldo\n\
    [2] Depositar dinheiro\n\
    [3] Sacar dinheiro\n\
    [4] Ecerrar o antendimento\n")
    acao = int(input())

    # Cadastro
    cont = 0 
    if acao == 0:
        conta = 0
        while cont != 'N':
            dados = {}
            print('Faça seu cadastro')

            nome = input('Digite seu nome: ')
            cpf = input ('Digite sue CPF: ')
            conta += 1
            saldo  = 0
                        
            dados['Nome'] = nome
            dados['CPF'] = cpf
            dados['Conta'] = conta
            dados['Saldo'] = saldo
            
            clientes.append(dados)
            print(clientes)
            print('Se desejar cadastrar novo cliente digite [S], se não digite [N].')
            cont = input().upper()


    
    # Acessar conta
    cpf_informado = input('Digite seu CPF: ')
    nome_cliente = None
    for dados in clientes:
        if dados['CPF'] == cpf_informado:
            nome_cliente = dados['Nome']
            break
    print()
    if nome_cliente is not None:
        print(f'Bem-Vindo(a) {nome_cliente}')
        print()
    else:
        print('CPF não encontrado.')

        
    # Verificar saldo
    
    if acao == 1:
        for dados in clientes:
            if dados['CPF'] == cpf_informado:
                
                saldo = dados['Saldo']
                print(f'Seu saldo é {saldo}')
                print()            
 
    
    # Depositar dinheiro
    if acao == 2:
        for dados in clientes:
            if dados['CPF'] == cpf_informado:
                saldo = dados['Saldo']
                deposito = float(input('Qual valor deseja depositar? '))
                dados['Saldo'] += deposito
                print(f'Seu saldo é R$', dados['Saldo'])
                print()
    
   
    # Sacar dinheiro

    if acao == 3:
        for dados in clientes:
            if dados['CPF'] == cpf_informado:
                print(dados['Saldo'])
                saque = float(input('Qual valor deseja sacar? '))
                if dados['Saldo'] >= saque:
                    dados['Saldo'] -= saque
                    print(f'Seu saldo é R$', dados['Saldo'])
                    print()
                else:
                    print('Não há saldo suficiente!')
                    print()

    # Encerrar o atendimento
    if acao == 4:
        print('Atendimento encerrado')
        break

