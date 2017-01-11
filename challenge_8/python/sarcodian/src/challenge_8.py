import random

class LinkedList(object):
    
    def __init__(self):
        self.linkedlist = {}
        self.step = 0
    
    def addNode(self, data):
        if self.step == 0:
            self.linkedlist[self.step] = [self.step + 1, random.randrange(0, 1, 1), data]
        else:
            self.linkedlist[self.step] = [self.step + 1, random.randrange(0, self.step, 1), data]
        self.step += 1
    
    def shuffleNodes(self):
        for i in self.linkedlist.keys():
            self.linkedlist[i] = [self.linkedlist[i][0],random.randrange(0, self.step, 1), self.linkedlist[i][2]]

    def printList(self):
        for i in self.linkedlist.keys():
            if i == 0:
                print('Head[{},{}][{}]->'.format(self.linkedlist[i][0], self.linkedlist[i][1], self.linkedlist[i][2]), end = "")
            elif i == self.step-1:
                print('[{},{}][{}]->Null'.format(self.linkedlist[i][0], self.linkedlist[i][1], self.linkedlist[i][2]))
            else:
                print('[{},{}][{}]->'.format(self.linkedlist[i][0], self.linkedlist[i][1], self.linkedlist[i][2]), end = "")

    def deepCopy(self):
        deepcopy = LinkedList()
        for i in self.linkedlist.keys():
            deepcopy.addNode(self.linkedlist[i][2]+"'")
            deepcopy.linkedlist[i][1] = self.linkedlist[i][1]
        return deepcopy
                
LL = LinkedList()
LL.addNode('A')
LL.addNode('B')
LL.addNode('C')
LL.addNode('D')
LL.printList()
LL.shuffleNodes()
LL.printList()
LL2 = LL.deepCopy()
LL2.printList()
LL2.shuffleNodes()
LL.printList()
LL2.printList()
