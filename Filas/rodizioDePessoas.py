def passarPessoa(filaPessoas):
  
  if len(filaPessoas) > 0:

    pessoaFrente = filaPessoas.pop(0)
    
    filaPessoas.append(pessoaFrente)
    
    return filaPessoas
  
  else:
    print("A fila está vazia.")
    return filaPessoas


filaPessoas = []

while True:

  nomePessoa = input("Digite o nome da pessoa que deseja fazer o rodízio (ou pressione Enter para parar): ")
    
  if nomePessoa == "":
    print("Programa Finalizado!")
    break
  
  filaPessoas.append(nomePessoa)
  
  filaPessoas = passarPessoa(filaPessoas)
  
  print(f"Nova configuração da fila: { filaPessoas}")
