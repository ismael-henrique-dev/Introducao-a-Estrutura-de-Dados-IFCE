class Fila:
  def __init__(self):

    self.fila = []

  def enfileirar(self, item):

    self.fila.append(item)

  def desenfileirar(self):

    if not self.vazia():

      return self.fila.pop(0)

  def vazia(self):

    return len(self.fila) == 0

  def inverter(self):

    if not self.vazia():
      
      elem = self.desenfileirar()
      self.inverter()
      self.enfileirar(elem)

fila = Fila()

while True:

  print("1. Enfileirar um item")
  print("2. Desenfileirar um item")
  print("3. Inverter a fila")
  print("4. Sair")

  opcao = int(input("Escolha uma opção: "))
  
  if opcao == 1:

    item = input("Digite o item a ser enfileirado: ")
    fila.enfileirar(item)

  elif opcao == 2:

    if fila.vazia():
      print("A fila está vazia.")
    else:
      print("Item desenfileirado: ", fila.desenfileirar())

  elif opcao == 3:

    fila.inverter()
    print("Fila invertida.")

  elif opcao == 4:
    
    break

  else:

    print("Opção inválida. Tente novamente.")
