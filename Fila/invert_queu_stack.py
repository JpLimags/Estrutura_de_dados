class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLinkedList:
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
        self.stack = StackUsingLinkedList()

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

    def invert(self):

        if self.stack.is_empty():
            return

        # Utilizamos uma pilha auxiliar para inverter a ordem dos elementos
        temp_stack = StackUsingLinkedList()
        
        while not self.stack.is_empty():
            temp_stack.push(self.stack.pop())

        self.stack = temp_stack

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Fila original:")
    while True:
        item = queue.dequeue()
        if item is None:
            break
        print(item)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("\nInvertendo a fila:")
    queue.invert()

    while True:
        item = queue.dequeue()
        if item is None:
            break
        print(item)