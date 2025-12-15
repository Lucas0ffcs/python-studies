from os import strerror

try:
    file = open('newtext.txt', 'wt')  # Um novo arquivo (newtext.txt) será criado.
    for i in range(10):
        s = "line #" + str(i + 1) + "\n"
        for char in s:
            file.write(char)
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
