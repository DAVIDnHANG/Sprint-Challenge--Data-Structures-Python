from doubly_linked_list import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.current.value = item
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head

    def get(self):
       #given
        list_buffer_contents = []

        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------
class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current += 1

        if self.current == self.capacity:
            self.current = 0

    def get(self):
        temp = []
        for i in self.storage:
            if i is not None:
                temp.append(i)
        return temp
