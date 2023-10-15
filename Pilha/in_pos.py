class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("A pilha está vazia")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("A pilha está vazia")

    def size(self):
        return len(self.stack)


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    output = []  # Lista para armazenar a expressão pós-fixa
    stack = Stack()  # Pilha para operadores

    for char in expression:
        if char.isalnum():
            output.append(char)  # Adiciona operandos diretamente à saída
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Remove o '(' da pilha
        else:
            # Processa operadores
            while not stack.is_empty() and stack.peek() in precedence and precedence[stack.peek()] >= precedence[char]:
                output.append(stack.pop())
            stack.push(char)

    # Despeja os operadores restantes da pilha
    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)


# Exemplo de uso
infix_expression = "3 + 5 * ( 2 - 8 )"
postfix_expression = infix_to_postfix(infix_expression)
print("Expressão infixa:", infix_expression)
print("Expressão pós-fixa:", postfix_expression)
