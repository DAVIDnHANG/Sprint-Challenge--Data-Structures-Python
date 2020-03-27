from dll_stack import Stack
from dll_queue import Queue

class BinarySearchTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    #insert values into tree
    def insert(self, value):
        #baseCase for BST
        if self.value is None:
            self.value = value
            return
        #go left
        if value < self.value:
            #check if end of BST
            if not self.left:
                self.left = BinarySearchTree(value)
            else:#move left side
                return self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: #move down right side
                return self.right.insert(value)

    #check if it has duplicates
    def contains(self, target):
        #check if string == string
        if target == self.value:
            return True
        #look left
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        #end if self.right is none
        else:
            if not self.right:
                return False
            else: #keep looking right side
                return self.right.contains(target)

    def get_max(self):
        #right side at the end of the list
        if self.right is None:
            return self.value
        #right side
        else:
            return self.right.get_max()