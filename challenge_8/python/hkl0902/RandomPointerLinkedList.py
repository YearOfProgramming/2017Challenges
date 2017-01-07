class RandomPointerLinkedList:
    def __init__(self, root, next, random):
        self.root = root
        self.next = next
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

    # Returns a list with the value of root for each LinkedList in self
    def rootsToList(self):
        return [l.root for l in self]

    # Returns a list with the value of the index of random
    def randomToList(self):
        return [self.get(l.random) for l in self]

    # Returns the index of L where L is a linked list in self. None otherwise
    def get(self, l):
        if not l:
            return None
        index = 0
        for link in self:
            if l == link:
                self.current = self
                return index
            index += 1

    # Returns a deep copy of self
    def makeDeepCopy(self):
        roots = self.rootsToList()
        newRoots = [str(root) + "\'" for root in roots]
        lists = [RandomPointerLinkedList(root, None, None) for root in newRoots]
        randomIndeces = self.randomToList()

        # Set up the next
        for i in range(len(lists)):
            if i == len(lists) - 1:
                lists[i].next = None
            else:
                lists[i].next = lists[i+1]

        # Set up the random
        for list, r in zip(lists, randomIndeces):
            lists[i].random = lists[r]

        return lists[0]
