#Estutura Base Fila
class Fila:
  def __init__(self):
    self.fila = []

  def enqueue(self, el):
    return self.fila.append(el)
  
  def dequeue(self):
    if not self.fila:
      return self.fila.pop(0)
    else:
      return "Lista Vazia"
  
  def front(self):
    return self.fila[0]
  
  def isEmpty(self):
    if not self.fila:
      return True
    else:
      return False
    
fila = Fila()

class Pilha:
  def __init__(self):
    self.pilha = []

  def push(self, el):
    self.pilha.append(el)
  
  def pop(self):
    self.pilha.pop()

  def peek(self):
    if not self.pilha:
      return self.pilha[-1]
    else:
      return False
  
  def isEmpty(self):
    if not self.fila:
      return True
    else:
      return False
    
pilha = Pilha()

pilha.peek()