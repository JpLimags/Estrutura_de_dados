class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            print("A pilha está vazia")

        item = self.top.data
        self.top = self.top.next

        return item

    def peek(self):
        if self.is_empty():
            print("A pilha está vazia")
        
        return self.top.data

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next

        return count
    
    def is_palindrome(input_string):
    # Remove espaços e converte para minúsculas
        input_string = input_string.replace(" ", "").lower()
        
        # Inicializa a pilha
        stack = Stack()

        # Adiciona os caracteres à pilha
        for char in input_string:
            stack.push(char)

        # Reconstroi a string invertida
        reversed_string = ""
        while not stack.is_empty():
            reversed_string += stack.pop()

        # Compara a string original com a invertida
        return input_string == reversed_string



# Exemplo de uso
#stack = Stack()
#stack.pop()
#stack.pop()

input_str = "Ana"
print(f"A string '{input_str}' é um palíndromo? {Stack.is_palindrome(input_str)}")

input_str = "hello"
print(f"A string '{input_str}' é um palíndromo? {Stack.is_palindrome(input_str)}")