from entity.Strategy import RandomStrategy


class Node:
    def __init__(self, data, next):
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self, listi: [], strategy=RandomStrategy()):
        self.strategy = strategy
        self.size = 0
        self.head = None
        self.__init_listi(listi)

    def __init_listi(self, listi):
        for f in listi:
            self.push(f)

    def pop_strategy(self):
        return self.pop(self.get_next_index())

    def get_next_index(self):
        return self.strategy.compute(self.get_size())

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        if data is None:
            raise ValueError()

        new_node = Node(data, None)

        if self.size == 0:
            self.head = new_node
            self.size += 1
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        self.size += 1

    def pop(self, i):
        if i >= self.size:
            raise ValueError()

        self.size -= 1
        node = self.head
        node_next = self.head

        if self.size == 0:
            self.head = None
            return node.data

        if i == 0:
            self.head = self.head.next
            return node.data

        for i in range(i):
            if i != 0:
                node = node.next
            node_next = node.next

        node.next = node_next.next

        return node_next.data

    def get_size(self):
        return self.size
