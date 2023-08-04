n = int(input('Digite um numero: '))

fibonacci = [1, 1]

for i in range(2,n):
 fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci) 
