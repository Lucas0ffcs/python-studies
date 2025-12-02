class Stack:
    def __init__(self):
        self.__stack_list = [] #colocar sublinhado antes do atributo torna-o privado como private em java


stack_object = Stack()
print(len(stack_object.__stack_list))
