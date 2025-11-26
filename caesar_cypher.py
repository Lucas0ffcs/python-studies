text = input("Enter the text to be encrypted:\n")
key = int(input("Enter the key of the cypher:\n"))
cypherlist = []

for ch in text:
    cont = 0
    if ch.isdigit() or ch.isspace():
        cypherlist[cont].append(ch)
        continue
    cypherlist[cont].append(chr(ord(ch)+key))
    cont += 1
cypher = "".join(cypherlist)
print(cypher)




