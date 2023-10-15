class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None

        data = self.top.data
        self.top = self.top.next
        return data

class Queue:
    def __init__(self):
        self.stack = Stack()

    def is_empty(self):
        return self.stack.is_empty()

    def enqueue(self, data):
        self.stack.push(data)

    def dequeue(self):
        # Transferimos os elementos da pilha para outra pilha para inverter a ordem
        temp_stack = Stack()

        while not self.stack.is_empty():
            temp_stack.push(self.stack.pop())

        # Removemos o primeiro elemento da pilha temporária
        if not temp_stack.is_empty():
            data = temp_stack.pop()
        else:
            data = None

        # Transferimos os elementos de volta para a pilha original
        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop())

        return data


def invert_first_k_elements(queue, k):
    if k <= 0:
        return

    # Usamos uma pilha para armazenar os primeiros k elementos
    stack = Stack()
    for _ in range(min(k, queue_size(queue))):
        stack.push(queue.dequeue())

    # Reinserimos os elementos na fila na ordem invertida
    while not stack.is_empty():
        queue.enqueue(stack.pop())

    # Movemos os elementos restantes para uma lista
    remaining_elements = []
    while not queue.is_empty():
        remaining_elements.append(queue.dequeue())

    # Movemos os elementos da lista de volta para a fila
    for element in remaining_elements:
        queue.enqueue(element)


def queue_size(queue):
    size = 0
    current = queue.stack.top
    while current:
        size += 1
        current = current.next
    return size


# Exemplo de uso
if __name__ == "__main__":
    fila = Queue()

    # Adiciona elementos à fila
    for i in range(11, 21):
        fila.enqueue(i)

    print("Fila original:")
    while not fila.is_empty():
        print(fila.dequeue(), end=" ")

    print("\nInvertendo os primeiros 3 elementos:")
    for i in range(11, 21):
        fila.enqueue(i)

    k = 3
    invert_first_k_elements(fila, k)

    while not fila.is_empty():
        print(fila.dequeue(), end=" ")
