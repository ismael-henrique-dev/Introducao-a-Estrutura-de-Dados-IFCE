def intercalarListas(lista1, lista2):
    
  listaIntercalada = []

  tamList1 = len(lista1)
  tamList2 = len(lista2)
  maxTam = tamList1 + tamList2

  for i in range(maxTam):
    if i < tamList1:
      listaIntercalada.append(lista1[i])
    if i < tamList2:
      listaIntercalada.append(lista2[i])

  return listaIntercalada

lista1 = [1, 4, 5, 7]
lista2 = [2, 3, 6, 8, 10]
intercalada = intercalarListas(lista1, lista2)
print(f'Lista {intercalada}')
