clientes = []


# Menu

def menu():
    print("Digite qual ação você quer fazer:\n\
    [0] Criar conta\n\
    [1] Verificar saldo\n\
    [2] Depositar dinheiro\n\
    [3] Sacar dinheiro\n\
    [4] Ecerrar o antendimento\n")
    

# Cadastro

def armazenar():
    conta = 0
    dados = {}
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')
    conta += 1
    saldo = 0

    dados['Nome'] = nome
    dados['CPF'] = cpf
    dados['Conta'] = conta
    dados['Saldo'] = saldo

    clientes.append(dados)
    print(clientes)
    print()
    


# Saldo

def verificar_saldo():
    print('Acesse sua conta!')
    print()
    cpf_informado = input('Digite seu CPF: ')
    nome_cliente = None
    for dados in clientes:
        if dados['CPF'] == cpf_informado:
            nome_cliente = dados['Nome']
            break
    if nome_cliente is not None:
        print()
        print (f'Bem-vindo(a) {nome_cliente}')
        print()
    else:
        print()
        print ('CPF não encontrado')
        print()
    for dados in clientes:
        if dados['CPF'] == cpf_informado:
            saldo = dados['Saldo']
            print (f'Seu saldo é R${saldo:.2f}')
            print()
        
# Depósito

def depositar():
    print('Acesse sua conta!')
    print()
    cpf_informado = input('Digite seu CPF: ')
    nome_cliente = None
    for dados in clientes:
        if dados['CPF'] == cpf_informado:
            nome_cliente = dados['Nome']
            break
    if nome_cliente is not None:
        print()
        print (f'Bem-vindo(a) {nome_cliente}')
        print()
    else:
        print()
        print ('CPF não encontrado')
        print()
    for dados in clientes:
        if dados['CPF'] == cpf_informado:
            saldo = dados['Saldo']
            deposito = float(input('Qual valor deseja depositar? '))
            dados['Saldo'] += deposito
            print()
            print (f'Seu saldo é R$', dados['Saldo'])
        
# Saque
        
def sacar():
    print('Acesse sua conta!')
    print()
    cpf_informado = input('Digite seu CPF: ')
    nome_cliente = None
    for dados in clientes:
        if dados['CPF'] == cpf_informado:
            nome_cliente = dados['Nome']
            break
    if nome_cliente is not None:
        print()
        print (f'Bem-vindo(a) {nome_cliente}')
        print()
    else:
        print()
        print ('CPF não encontrado')
        print()
    for dados in clientes:
        if dados['CPF'] == cpf_informado:
            saque = float(input('Qual o valor deseja sacar? '))
            if dados['Saldo'] >= saque:
                dados['Saldo'] -= saque
                print()
                print (f'Seu saldo é R$', dados['Saldo'])
                print()
            else:
                print()
                print ('Não há saldo suficiente!')
                print()

# Encerramento 
       
def encerrar():
    print('Atendimento encerrado')