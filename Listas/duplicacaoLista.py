lista = [1, 2 ,3 ,3 ,4 ,5 ,3]
listaDuplicados = []
listaNaoDuplicados = []

print(lista)

for i in lista:
  if i in lista: # Se meu elemnto tiver na lista normal
    if i not in listaDuplicados: # Se meu elmento não tiver na lista eu add
      listaDuplicados.append(i)
    else:
      listaNaoDuplicados.append(i) # Se não eu caio fora

print(listaDuplicados)