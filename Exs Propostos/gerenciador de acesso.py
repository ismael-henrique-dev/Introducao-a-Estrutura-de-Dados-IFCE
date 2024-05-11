class Gerenciamento:

  def __init__(self):

    self.listaNormal = []
    self.listaUrgente = []
  
  def addSolicitacao(self, solicitacao, tipo):
    
    if tipo == 1:
      self.listaUrgente.append(solicitacao)
      print(self.listaUrgente)
    elif tipo == 2:
      self.listaNormal.append(solicitacao)
      print(self.listaNormal)
    else:
      print("Opção Inválida!")
    
  def atenderSolicitacao(self):

    if self.listaUrgente:
      print("Atendendo as solicitações urgentes: \n")
      solicitacao = self.listaUrgente.pop(0)
      print(f"Solicitação: {solicitacao}")
    elif self.listaNormal:
      print("Atendendo as solicitações normais: \n")
      solicitacao = self.listaNormal.pop(0)
      print(f"Solicitação: {solicitacao}")
   
  def cancelarSolicitacao(self, solicitacao, tipo):

    if tipo == 1 and solicitacao in self.listaUrgente:
      self.listaUrgente.remove(solicitacao)
      print("Solicitação urgente removida!")
    elif tipo == 2 and solicitacao in self.listaNormal:
      self.listaNormal.remove(solicitacao)
      print("Solicitação normal removida!")
    else:
      print("Essa solicitação não existe!")

  def consultarProximaSolicitacao(self, tipo):
    
    if tipo == 1:
      print(f'Próxima solicitação urgente: {self.listaUrgente[0]}')
    elif tipo == 2:
      print(f'Próxima solicitação normal: {self.listaNormal[0]}')
    else:
      return "Opção Inválida!"
  
gerenciador = Gerenciamento()

# Interação com o usuário

print("------ Gerenciador de Acesso ao Cliente -0,----- \n")

while True:
  
  resp = int(input("Menu de Opções: \n 1 - Adicionar Solicitação \n 2 - Atender Solicitação \n 3 - Cancelar Solicitação \n 4 - Consultar Próxima Solicitação \n 5 - Encerrar Programa \n"))

  if resp == 1:
    solicitacao = input("Informe sua solicitação: \n")
    tipoDeSolicitação = int(input("Informe o tipo de solicitação: [1 - Urgente | 2 - Normal] \n"))
    gerenciador.addSolicitacao(solicitacao, tipoDeSolicitação)
  elif resp == 2:
    gerenciador.atenderSolicitacao()
  elif resp == 3:
    solicitacao = input("Informe sua solicitação: \n")
    tipoDeSolicitação = int(input("Informe o tipo de solicitação: [1 - Urgente | 2 - Normal] \n"))
    gerenciador.cancelarSolicitacao(solicitacao, tipoDeSolicitação)
  elif resp == 4:
    gerenciador.consultarProximaSolicitacao(tipoDeSolicitação)
  elif resp == 5:
    print("Programa Finalizado! \n")
    break
  else:
    print("Opção Inválida! \n")
