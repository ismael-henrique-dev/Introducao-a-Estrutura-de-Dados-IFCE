def definir_prioridade():
  print('Defina a prioridade da tarefa: ')
  print('1 - alta || 2 - Média || 3 - baixa')
  prioridade = int(input())
  return prioridade

def processar_tarefa(fila):
    
    fila_alta = []
    fila_media = []
    fila_baixa = []

    for item in fila:
        if item[1] == 1:
            fila_alta.append(item)
        elif item[1] == 2:
            fila_media.append(item)
        elif item[1] == 3:
            fila_baixa.append(item)

    fila_alta.extend(fila_media)
    fila_alta.extend(fila_baixa)

    return fila_alta
  
# Fila
class Impressora:

    def __init__(self):
        self.fila = []

    def is_empty(self):

        if not self.fila:
            return True
        else:
            return False

    def enqueue(self, item):
        prioridade = definir_prioridade()
        self.fila.append([item, prioridade])

    def dequeue(self):
        if not self.fila:
            print('Fila vazia')
        else:
            self.fila.pop(0)

    def front(self):
        fila = processar_tarefa(self.fila)
        if fila:
            return fila[0]
        else:
            print('Fila vazia')

    def cancelar_tarefa(self, tarefa):
        for count in range(len(self.fila)):
            if self.fila[count][0] == tarefa:
                self.fila.pop(count)
                print('Tarefa cancelada:', tarefa)
                return
        print('Não existe essa tarefa!')

gerenciador = Impressora()

while True:
    
    print("\n1 - Adicionar tarefa")
    print("2 - Processar tarefas")
    print("3 - Cancelar tarefa")
    print("4 - Verificar próxima tarefa")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite o nome da tarefa: ")
        gerenciador.enqueue(tarefa)
    elif opcao == "2":
        gerenciador.dequeue()
    elif opcao == "3":
        tarefa = input("Digite o nome da tarefa a ser cancelada: ")
        gerenciador.cancelar_tarefa(tarefa)
    elif opcao == "4":
        proxima_tarefa = gerenciador.front()
        if proxima_tarefa:
            print("Próxima tarefa:", proxima_tarefa)
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
