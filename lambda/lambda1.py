nums = [3, 1, 4, 1, 5, 9, 2]

dobrado = list(map(lambda x: x*2, nums))

stringer = list(map(lambda x: str(x), dobrado))

quadrado = list(map(lambda x: x*x, nums))

soma5 = list(map(lambda x: x+5, nums))

print(nums)
print("Dobro de nums ", dobrado)
print("Dobro de nums em Strings ", stringer)
print("Quadrado de nums ", quadrado)
print("Soma 5 a nums ", soma5)