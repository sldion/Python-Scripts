
class Node:

    def __init__(self,value):

        self.data = value
        self.next = None
        self.min  = None

class Stack:
    top = Node(None)

    def pop(self):
        if(self.top.data != None ):
            item = Node(self.top.data)
            self.top = self.top.next
            return item
        else:
            return None

    def push(self, item):

        if (self.top.min == None):
            self.top.min = item
        if item < self.top.min:
            t = Node(item)
            t.min = item
            t.next = self.top
            self.top = t
        else:
            t = Node(item)
            t.min = self.top.min
            t.next = self.top
            self.top = t

    def getMin(self):
        return self.top.min

    def isOnlyElement(self):

        if(self.top.next == None):
            return True
        else:
            return False

    def sortStackAscending(self):

        sortList = []

        while(self.top.next.data != None):
            sortList.append(self.top.next.data)
            self.top = self.top.next

        sortList = sorted(sortList)

        for item in sortList:

            x = Node(item)
            x.next = self.top
            self.top = x






class stackOfStacks:
    listOfStacks = []



    def push(item):
        last = getLastStack()
        return 0


# implements a queue with two stacks
class shittyQueue:

    firstStack = Stack()
    last  = Stack()

    def enqueue(self,item):

        if(self.first.data == None):
            Stack1.push(item)
            back = Node(item)
            first = back
        else:
            stack2.push(item)


    def dequeue(self,item):

        if(stack1.isOnlyElement()):

            x = stack1.pop()

            while(not stack2.isOnlyElement()):

                stack1.push(stack2.pop())
