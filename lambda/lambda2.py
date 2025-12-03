a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

somaListas = list(map(lambda x, y: x + y, a, b))

print(a)
print(b)
print("Soma A e B: ", somaListas)

multipListas = list(map(lambda x, y: x*y, a, b))
print("Multiplica itens da lista de mesmo indice: ", multipListas)