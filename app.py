def menu():
    
    menu = '''
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar contas
    [6] Novo Usuario
    [0] Sair
    =>'''

    return menu

def realiza_deposito(deposito,saldo,extrato): # opção 1

    print('######################### Deposito ##########################')
    print()
    deposito = float(input('Informe o valor que deseja depositar: R$ '))
    print()
    print('##############################################################')
    print()
    if deposito <= 0:
        print('Não é possivel depositar saldos negativo')
        print('Por gentileza, tente realizar a operação novamente')
    else:
        saldo += deposito
        extrato += f'Deposito R$ {deposito:.2f}\n'
        print(f'Valor depositado com sucesso R$ {deposito:.2f}')
        print()
        print('##############################################################')
    return saldo, extrato

def realizar_saque(numero_saques,saldo,saque,extrato,limite,LIMITE_SAQUES):  # opção 2
    print('######################### Saque ##########################')
    print()
    saque = float(input('Informe o valor que deseja sacar: R$ '))
    print()

    if numero_saques >= LIMITE_SAQUES:

        print('Limites de saques diarios excedidos')
        print()
        print('##############################################################')         

    elif saque > limite:
        print('Saque fora do limite autorizado')
        print()
        print('##############################################################')
                
    elif saque > saldo:

        print('Valor indisponível para saque')
        print()
        print('##############################################################')
                
    else:
        numero_saques += 1
        #print(numero_saques) #teste
        saldo -= saque
        extrato += f'Saque: R$ -{saque:.2f}\n'
        print(f'Saque realizado com sucesso R$ -{saque:.2f}')
        print()
        print('##############################################################')

    return saldo, extrato, saque, numero_saques

def verifica_extrato(extrato, saldo): # opção 3
    print('######################### Extrato ##########################')
    print()

    if extrato == '':
          
        print(f'Saldo atual: R$ {saldo:.2f}')
        print()
        print('Extrato atual')
        print('Não foram realizadas movimentações')
        print()
        print('##############################################################')
    else:
        print(f'Operações realizadas:\nR$ {extrato}')
        print()
        print(f'Saldo em conta: R$ {saldo:.2f}')
        print('##############################################################')

    return extrato, saldo

def criar_conta (agencia, numero_conta, usuarios): # opção 4
    cpf = input('Informe o CPF (Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios) 

    if usuario:
        print('\n === Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\n Usuário não encontrado, fluxo de criação de conta encerrado')

def listar_contas(contas): #opção 5
    for conta in contas:
        print(f" Agência:{conta['agencia']}\n C/C:{conta['numero_conta']}\n Titular:{conta['usuario']['nome']}")
        print()
        print("=" * 100)

def novo_usuario(usuarios): # opção 6
    cpf = input('Informe o CPF (Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Usuário já existente com esse número de CPF')

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informa a data de nascimento (dd-mm-aaaa): ')
    print('EX: Endereço: Rua B, 20 - Lapa - Rio de Janeiro/RJ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('=== Usuário criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios): # filtra usuario

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def main():
    usuarios = []
    contas = []
    deposito = 0
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saque = 0  

    while True:
        #Menu
        print(menu())
        try:
            opcao = int(input())
        except ValueError:
            print('Opção Inválida')
            continue
        print()

        if opcao == 1: # Deposito
            saldo, extrato = realiza_deposito(deposito,saldo,extrato)

        elif opcao == 2: # Saque
            saldo, extrato,saque, numero_saques = realizar_saque(numero_saques,saldo,saque,extrato,limite,LIMITE_SAQUES)
                
        elif opcao == 3: # Extrato
            verifica_extrato(extrato, saldo)

        elif opcao == 4: # Criar conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6: # Novo usuáio
            novo_usuario(usuarios)

        elif opcao == 0:
            print('Sair')
            break
        else:
            print('Opção inválida, por favor selecione a operação desejada.')

main()