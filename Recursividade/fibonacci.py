# 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584

def fibinacciRecursivo(num):
  if num <= 1:
    return num
  else:
    return fibinacciRecursivo(num - 1) + fibinacciRecursivo(num - 2)
  
num = int(input("Digite um número para saber seu Fibonacci: \n"))
res = fibinacciRecursivo(num) 
print(res)