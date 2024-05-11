class Lista:
  def __init__(self):
    self.lista = []
  def adicionar(self, element):
    self.lista.append(element)
    print(self.lista)
  def buscar(self, element):
    if element in self.lista:
      print(f'Elemento encontrado {element} \n')
    else:
      print("Elemento não encontrado! \n")
  def remover(self, element):
    if element in self.lista:
      self.lista.remove(element)
      print(self.lista)
    else:
      print(f"Elemento {element} não encontrado na lista.")
  def imprimirTodos(self):
    for i in self.lista:
      print(f"Elemento {i}")

test = Lista()

test.adicionar("Macaxeira")
test.adicionar("Caxote")

test.remover("caixo")
test.remover("Macaxeira")

test.adicionar("Banana")

test.imprimirTodos()
test.buscar("Banana")