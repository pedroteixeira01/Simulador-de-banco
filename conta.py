import uuid
import os

class conta(object):
     
    def __init__(self, documento='?', credito=0):
        
        self.credito = credito
        self.documento = documento
    def cria_conta(self,documento):
        
        id = str(uuid.uuid1())
        self.documento = documento
        path = os.getcwd() + '/contas/'
        try:
            
            os.mkdir(path)
            conta = open(path + id,'w')
            conta.write('\nid da conta:\n%s' %id)
            conta.write('\ndocumento da conta:\n%s' %self.documento)
            conta.write('\ncredito da conta:\n%d' %self.credito)
            conta.close()
            conta = open(path + id,'r')
            return conta.read()
            conta.close()
        except FileExistsError:
            
            conta = open(path + id,'w')
            conta.write('\nid da conta:\n%s\n' %id)
            conta.write('documento da conta:\n%s\n' %self.documento)
            conta.write('credito da conta:\n%d' %self.credito)
            conta.close()
            conta = open(path + id,'r')
            return conta.read()
            conta.close()
    def ver_saldo(self, identf):
        
        path = os.getcwd() + '/contas/'
        conta = open(path + identf,'r')
        return '\nSaldo: ' + conta.readlines()[6]
        conta.close()
    def ver_documento(self, identf):
        
        path = os.getcwd() + '/contas/'
        conta = open(path + identf,'r')
        return '\nDocumento: ' + conta.readlines()[4]
    def listar_contas(self):

        path = os.getcwd() + '/contas/'
        contas = [arq for arq in os.listdir(path)]
        return contas
    def encontrar(self, encontra):
        
        self.encontra = encontra
        path = os.getcwd() + '/contas/'
        lista = conta.listar_contas()
        for i in lista:
            if encontra in i:
                
                return i    
    def transacao(self, id_trans, id_rece, operacao, valor):
        
        self.id_trans = id_trans
        self.id_rece = id_rece
        self.operacao = operacao
        self.valor = valor
        pathc = os.getcwd() + '/contas/'
        patht = os.getcwd() + '/transacoes/'
        try:
            
            os.mkdir(patht)
            conta1 = open(pathc + id_trans, 'r')
            saldo = conta1.readlines()
            if operacao == 'pagamento' or operacao == 'pagamento à vista':
                if int(saldo[5]) >= valor:
                    saldo[6] = int(saldo[6]) - valor
                    saldo[6] = str(saldo[6])
                    conta1 = open(pathc + id_trans, 'w')
                    conta1.writelines(saldo)
                    transf = open(patht + id_trans, 'a')
                    transf.write(
                        'tranferencia realizada por: %s\npara: %s\nvalor: %.2f\noperacao: %s\n\n'
                        %(id_trans, id_rece, valor, operacao))
                    verif = True
                else:
                    verif = False
                    print('\nsaldo insuficiente\n')
                conta1.close()
                conta2 = open(pathc + id_rece, 'r')
                saldo2 = conta2.readlines()
                if verif:
                    saldo2[6] = int(saldo2[6]) + valor
                    saldo2[6] = str(saldo2[6])
                    conta2 = open(pathc + id_rece, 'w')
                    conta2.writelines(saldo2)
                conta2.close()
                return '\n Transferência concluída\n '
            elif operacao == 'saque':
                if int(saldo[6]) >= valor:
                    saldo[6] = int(saldo[6]) - valor
                    saldo[6] = str(saldo[6])
                    conta1 = open(pathc + id_trans, 'w')
                    conta1.writelines(saldo)
                    transf = open(patht + id_trans, 'a')
                    transf.write(
                        'saque realizado no valor de R$%.2f\n\n'
                        %valor)
                    return '\nSaque conluído\n'
        except FileExistsError:
            conta1 = open(pathc + id_trans, 'r')
            saldo = conta1.readlines()
            if operacao == 'pagamento' or operacao == 'pagamento à vista':
                if int(saldo[6]) >= valor:
                    saldo[6] = int(saldo[6]) - valor
                    saldo[6] = str(saldo[6])
                    conta1 = open(pathc + id_trans, 'w')
                    conta1.writelines(saldo)
                    transf = open(patht + id_trans, 'a')
                    transf.write(
                        'tranferencia realizada por: %s\npara: %s\nvalor: %.2f\noperacao: %s\n\n'
                        %(id_trans, id_rece, valor, operacao))
                    verif = True
                else:
                    verif = False
                    print('\nsaldo insuficiente\n')
                conta1.close()
                conta2 = open(pathc + id_rece, 'r')
                saldo2 = conta2.readlines()
                if verif:
                    saldo2[6] = int(saldo2[6]) + valor
                    saldo2[6] = str(saldo2[6])
                    conta2 = open(pathc + id_rece, 'w')
                    conta2.writelines(saldo2)
                conta2.close()
                return '\nTransferência concluída\n'
            elif operacao == 'saque':
                if int(saldo[6]) >= valor:
                    saldo[6] = int(saldo[6]) - valor
                    saldo[6] = str(saldo[6])
                    conta1 = open(pathc + id_trans, 'w')
                    conta1.writelines(saldo)
                    transf = open(patht + id_trans, 'a')
                    transf.write(
                        'saque realizado no valor de R$%.2f\n\n'
                        %valor)
                    return '\nSaque concluído\n'
    def extrato(self, identf):
        
        patht = os.getcwd() + '/transacoes/'
        conta = open(patht + identf, 'r')
        return conta.read()
conta = conta()
