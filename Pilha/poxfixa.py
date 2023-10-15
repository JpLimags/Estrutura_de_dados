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
    
    def evaluate_postfix(expression):
        stack = Stack()
        operators = set(['+', '-', '*', '/'])

        for char in expression.split():
            if char not in operators:
                # Se for um operando, converte para int e coloca na pilha
                stack.push(int(char))
            else:
                # Se for um operador, pop dos operandos da pilha e aplique a operação
                operand2 = stack.pop()
                operand1 = stack.pop()

                if char == '+':
                    result = operand1 + operand2
                elif char == '-':
                    result = operand1 - operand2
                elif char == '*':
                    result = operand1 * operand2
                elif char == '/':
                    result = operand1 / operand2

                # Empurra o resultado de volta na pilha
                stack.push(result)
        # O resultado final estará no topo da pilha
        return stack.peek()


# Exemplo de uso
expression1 = "5 3 +"
result1 = Stack.evaluate_postfix(expression1)
print(f"Resultado da expressão '{expression1}': {result1}")