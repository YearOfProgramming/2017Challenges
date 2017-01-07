class RandomPointerLinkedList:
    def __init__(self, root, next, random):
        self.root = root
        self.next = next
        self.random = random
        self.current = self

    @property
    def root(self):
        return self.root

    @property
    def next(self):
        return self.next

    def random(self):
        return self.random

    def __iter__(self):
        return self

    def next(self):
        if self.current.next:
            curr = self.current
            self.current = self.current.next
            return curr
        self.current = self
        raise StopIteration

    @property
    def length(self):
        if not self:
            return 0
        if self.next:
            return 1 + self.next.length
        else:
            return 1

    def rootsToList(self):
        return [l.root for l in self]

    def nextToList(self):
        return [l.next.root if l.next else None for l in self]

    def randomToList(self):
        return [l.next.random if l.next else None for l in self]

    # Returns the i'th linked list. self is at 0
    def get(i):
        index = 0
        for l in self:
            if index == i:
                self.current = self
                return l
            index += 1

    
