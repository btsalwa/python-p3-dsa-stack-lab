class Stack:
    '''LIFO Stack implementation'''

    def __init__(self, items=None, limit=None):
        '''Initialize Stack with list and limit'''
        if items is None:
            self.items = []
        else:
            self.items = items

        if limit is None:
            self.limit = float('inf')
        else:
            self.limit = limit

    def push(self, item):
        '''Push item onto stack, respecting limit'''
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        '''Pop item off stack, return None if empty'''
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def size(self):
        '''Return number of items in stack'''
        return len(self.items)

    def isEmpty(self):
        '''Return True if stack is empty, False otherwise'''
        return len(self.items) == 0

    def full(self):
        '''Return True if stack is full, False otherwise'''
        return len(self.items) == self.limit

    def search(self, item):
        if item in self.items:
            return self.items.index(item)
        else:
            return -1