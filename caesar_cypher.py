text = input("Enter the text to be encrypted:")
key = int(input("Enter the key of the cypher:"))
cypher = []

for ch in text:
    cont = 0
    if ch.isdigit() or ch.isspace():
       continue
    cypher[cont].append(chr(ord(ch)+key))






