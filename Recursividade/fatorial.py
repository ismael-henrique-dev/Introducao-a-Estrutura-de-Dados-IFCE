def fatorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * fatorial(num-1)
  
num = int(input("Digite um numero para seu fatorial: \n"))
res = fatorial(num)
print(res)