stream = open("notas.txt", "rb")

byter = bytearray(stream.read())

print(byter)
