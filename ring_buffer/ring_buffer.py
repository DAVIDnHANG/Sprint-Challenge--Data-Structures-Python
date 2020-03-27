from doubly_linked_list import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        while(current is not None):
            self.storage.add_to_head(item)
        if self.current is None:
            self.current = 0

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        while(self.storage is not None):
            list_buffer_contents.append(self.storage.remove_from_tail())
            print(list_buffer_contents, 'asd')
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
