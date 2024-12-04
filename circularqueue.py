class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None]*k
        self.front = 0
        self.rear = -1
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.k
    
    def enQueue(self, data):
        if self.isFull():
            print("Queue is full")
            return
        self.rear = (self.rear+1)%self.k
        self.queue[self.rear] = data
        self.size += 1
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        self.queue[self.front] = None
        self.front = (self.front+1)%self.k
        self.size -= 1
    
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    
    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        i = self.front
        while i != self.rear:
            print(self.queue[i], end=' ')
            i = (i+1)%self.k
            print(self.queue[self.rear])
            
q = CircularQueue(5)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.enQueue(6)
q.deQueue()
q.deQueue()
q.enQueue(7)
q.enQueue(8)
q.enQueue(9)
q.printQueue()
print(q.getFront())
print(q.getRear())
# Output
# 3 4 5 7 8
# 3
# 8
