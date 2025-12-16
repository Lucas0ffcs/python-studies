from operator import indexOf
from os import strerror

entrada = input("Digite o nome do arquivo:\n")
try:
    stream = open(entrada, "r")

except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)
texto = stream.read().lower()

histo = {}

for l in texto:
    if l in histo:
        histo[l] += 1
    else:
        histo[l] = 1

for i in histo:
    print(i + ":" + str(histo[i]))


