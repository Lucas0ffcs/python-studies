text = input("Enter the text to be encrypted:\n")
key = int(input("Enter the key of the cypher:\n"))

cypher = ""  # string final

for ch in text:
    if ch.isdigit() or ch.isspace():
        cypher += ch
    else:
        cypher += chr(ord(ch) + key)

print(cypher)



