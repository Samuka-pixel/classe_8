i = int(input("Digite um número inicial: "))
h = int(input("Digite um número final: "))
j = int(input("digite o número de passos: "))
print(f'os números entre {i} e {h} com o imcremento de {j} são:')
for x in range(i,h+1, j):
    print(x, end=' ')