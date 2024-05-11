def converterBinario(numInt):
  result = bin(numInt)
  return str(result)

num = int(input("Digite um num qualquer: \n"))

print(converterBinario(num))