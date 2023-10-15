class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def is_empty(self):
        return self.queue1.is_empty() and self.queue2.is_empty()

    def push(self, data):
        self.queue1.enqueue(data)

    def pop(self):
        if self.is_empty():
            return None

        # Transferir elementos de queue1 para queue2, mantendo apenas o último elemento
        while self.queue1.peek() is not None:
            item = self.queue1.dequeue()
            if self.queue1.peek() is not None:
                self.queue2.enqueue(item)

        # Swap queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return item


class Queue:
    def __init__(self):
        self.stack = StackUsingQueue()

    def enqueue(self, item):
        self.stack.push(item)

    def dequeue(self):
        if self.stack.is_empty():
            return None

        # Recursivamente retiramos os elementos da pilha e os enfileiramos novamente
        item = self.stack.pop()
        if self.stack.is_empty():
            return item

        dequeued_item = self.dequeue()
        self.stack.push(item)
        return dequeued_item



# Função para inverter a pilha usando fila
def invert_stack(stack):
    if stack.is_empty():
        return

    temp_queue = Queue()

    # Transferir elementos da pilha para a fila
    while not stack.is_empty():
        item = stack.pop()
        temp_queue.enqueue(item)

    # Transferir elementos da fila de volta para a pilha
    while not temp_queue.is_empty():
        item = temp_queue.dequeue()
        stack.push(item)


# Exemplo de uso
if __name__ == "__main__":
    stack = StackUsingQueue()

    # Empilhar alguns elementos
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Pilha original:")
    while not stack.is_empty():
        print(stack.pop())

    # Inverter a pilha
    invert_stack(stack)

    print("\nPilha invertida:")
    while not stack.is_empty():
        print(stack.pop())






