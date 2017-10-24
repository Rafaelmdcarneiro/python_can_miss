class Fifo:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, node):
        if self.head is None:
            self.head = node
        if None is not self.tail:
            self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head is None:
            return None
        if self.head is self.tail:
            self.tail = None
        aux = self.head
        self.head = self.head.next
        return aux

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def contains(self, state):
        if self.head is None:
            return False
        aux = self.head
        while not aux is None:
            if state.isEqual(aux.state):
                return True
            aux = aux.next

        return False
