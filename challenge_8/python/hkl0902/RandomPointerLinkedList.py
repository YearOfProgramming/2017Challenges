class RandomPointerLinkedList:
    def __init__(self, root, next, random):
        self.root = root
        self.index = 0
        self.next = next
        if next:
            self.index = next.index + 1
        self.random = random
        self.current = self

    def __iter__(self):
        return self

    def __next__(self):
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

    # Returns a list of the roots in the linked lists
    # The root for self is at the end of the list
    def toList(self):
        return [l.root for l in self][::-1]

    # Returns a list of the index of the random linked list
    # The last element in the returned list is the random element's index for self
    # Assumes that all elements have a random
    def randomIndices(self):
        return [l.random.index for l in self][::-1]

    # Makes a deep copy
    def makeDeepCopy(self):
        allRoots = self.toList()
        allRandom = self.randomIndices()

        # Makes all the linked lists
        lists = [RandomPointerLinkedList(root, None, None) for root in allRoots]
        length = len(lists)

        # Adds all the next to all the LinkedLists in lists
        # it's i-1 because the allRoots and allRandom give values in reverse order
        for l, i in zip(lists, range(length)):
            if i == 0:
                l.next = None
            else:
                l.next = lists[i-1]

        
