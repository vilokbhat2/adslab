class FlexiQueue:
    default_size = 2
    def __init__(self):
        self.data = [None]*FlexiQueue.default_size
        self.front = 0
        self.count = 0
    
    def isEmpty(self):
        return self.count == 0
    
    def queueCount(self):
        return self.count
    
    def getFirst(self):
        if self.isEmpty():
            return None
        return self.data[self.front]
    
    def enqueue(self, ele):
        if self.count == len(self.data):
            self.resize(2*len(self.data))
        idx = (self.front + self.count)%len(self.data)
        self.data[idx] = ele
        self.count += 1
        
    def dequeue(self):
        if not self.isEmpty():
            ele = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front+1)%len(self.data)
            self.count -= 1
            if 0 < self.count < len(self.data)//4:
                self.resize(len(self.data)//2)
            return ele
        else:
            return None
        
    def resize(self, cap):
        old_data = self.data
        walk = self.front
        self.data = [None]*cap
        for i in range(self.count):
            self.data[i] = old_data[walk]
            walk = (walk+1)%len(old_data)
        self.front = 0
    
    def printQueue(self):
        for i in range(self.count):
            print(self.data[(self.front+i)%len(self.data)], end=' ')
        print()

q = FlexiQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.dequeue()
q.enqueue(7)
q.printQueue()
# Output: 3 4 5 6 7
