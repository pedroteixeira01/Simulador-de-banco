from conta import *

print('###########')
print('teste API')
print('###########')

while True:
    
    menu = input(
        '''
Crie sua conta ou entre com uma existente:

A) Criar uma conta
B) Entrar com uma conta existente
C) Sair
-> '''
        ).lower()
    if menu == 'a':
        
        doc = input('Digite o número de um documento válido -> ')
        print('\nSua conta está sendo criada...\n')
        criar = conta.cria_conta(doc)
        print('\nConta criada com sucesso. Anote com atenção os primeiros 5 dígitos do seu ID\n')
        print(criar)
        continue
    elif menu == 'b':
        
        ident = input('Digite os 5 primeiros elemetos de seu ID -> ')
        encontrar = conta.encontrar(ident)
        if not encontrar:
            
            print('\nconta inexistente\n')
        elif encontrar:
            
            print('\nconta encontratada\n')
            while True:
                
                menu2 = input('''
Bem vindo! O que deseja fazer hoje ?

A) Ver meu saldo
B) Ver o extrato
C) Ver meu documento cadastrado
D) Realizar uma transação
E) Logout                 
-> '''
            ).lower()
                if menu2 == 'a':
                    
                    print(conta.ver_saldo(encontrar))
                elif menu2 == 'b':
                    
                    print(conta.extrato(encontrar))
                elif menu2 == 'c':
                    
                    print(conta.ver_documento(encontrar))
                elif menu2 == 'd':
                    
                    while True:
                        tipo = input('''
Escolha o tipo de transação
A) Saque
B) À vista
C) Transferência
D) Voltar              
-> ''')
                        if tipo == 'a':
                            
                            val = int(input('Digite o valor da operação -> '))
                            if int(conta.ver_saldo(encontrar)[7:]) >= val:
                                
                                conta.transacao(encontrar, encontrar, 'saque', val)
                                print('\nOperação concluída')
                                continue
                        elif tipo == 'b':
                            
                            val = int(input('Digite o valor da operação -> '))
                            if int(conta.ver_saldo(encontrar)[7:]) >= val:
                                     
                                enviar = input('Digite os 5 primeiros dígitos do ID do receptor -> ')
                                env = conta.encontrar(enviar)
                                conta.transacao(encontrar, env, 'pagamento à vista', val)
                                print('Operação concluída')
                                continue
                        elif tipo == 'c':
                            
                            val = int(input('Digite o valor da operação -> ')) 
                            if int(conta.ver_saldo(encontrar)[7:]) >= val:
                                
                                enviar = input('Digite os 5 primeiros dígitos do ID do receptor -> ')
                                env = conta.encontrar(enviar)
                                conta.transacao(encontrar, enviar, 'pagamento', val)
                                print('Operação concluída')
                                continue
                        elif tipo == 'd':
                            break
                        else:
                            
                            print('opção inexistente')
                            continue
            
                elif menu2 == 'e':
                    break
                else:
                
                    print('opção inexistente')
            
        else:
            
            print('conta inexistente')
            continue
    elif menu == 'c':
        
        print('\nsaindo...')
        break
    else:
        
        print('Opção inexistente. Tente novamente')
        continue