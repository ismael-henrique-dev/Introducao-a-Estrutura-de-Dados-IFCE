# funções - Inserir, Atender Clientes e Mostrar a situação atual da Lista

class FiladeBanco:

    def __init__(self):

        self.fila = []

    def InserirCliente(self, cliente):

        self.fila.append(cliente)
        print(f"Cliente Inserido! \n Fila: {self.fila} \n")

    def AtenderClientes(self):

        if not self.fila:
            print("Fila Vazia... \n")
        else:
            print(f'Atendendo o cliente: {self.fila.pop(0)} \n')

    def VerFila(self):

        print(f'Situação atual da fila: {self.fila} \n')

gerente = FiladeBanco()

while True:

    resp = int(input("Menu de opções: \n 1 - Inserir Cliente \n 2 - Atender Cliente \n 3 - Ver Situação Atual da Fila \n 4 - Parar Programação \n "))

    if resp == 1:
        cliente = input("Digite o nome do cliente: \n")
        gerente.InserirCliente(cliente)
    elif resp == 2:
        gerente.AtenderClientes()
    elif resp == 3:
        gerente.VerFila()
    elif resp == 4:
        print("Programa Finalizado! \n")
        break
    else:
        print("Opção Inválida \n")
        