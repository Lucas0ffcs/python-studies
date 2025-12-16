stream = open("frases.txt", "w")

stream.write("Frase 1\n")
stream.write("Frase 2\n")
stream.write("Frase 3\n")
stream.write("Frase 4\n")
stream.write("Frase 5\n")

stream.close()

stream2 = open("frases.txt", "r")
cont = 0
for i in stream2:

    cont += 1

print(cont)