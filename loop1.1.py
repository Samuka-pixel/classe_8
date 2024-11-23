i = int(input("Digite um número inicial: "))
h = int(input("Digite um número final: "))
print(f'os números entre {i} e {h} são:')
for x in range(i,h+1):
    print(x, end=' ')