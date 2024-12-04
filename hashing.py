import numpy as np
class openHash:
    class Node:
        def __init__(self, aNum, name, phone, address):
            self.aNum = aNum
            self.name = name
            self.phone = phone
            self.address = address
            self.next = None
        
    def __init__(self):
        self.tablesize = 11
        self.hashTable = [None] * self.tablesize
        self.p = 13
        self.a = np.random.randint(1, (self.p-1))
        self.b = np.random.randint(0, (self.p-1))
    
    def hashCodeGenerator(self, aNum):
        hashCode = 0
        aNum = str(aNum)
        for ch in aNum:
            hashCode = hashCode<<5
            hashCode = hashCode + ord(ch)
        return hashCode
    
    def compression(self, hashCode):
        return ((hashCode*self.a + self.b)%self.p)%self.tablesize
    
    def hash(self, aNum):
        hashCode = self.hashCodeGenerator(aNum)
        index = self.compression(hashCode)
        return index
    
    def isMember(self, aNum):
        index = self.hash(aNum)
        cur = self.hashTable[index]
        while cur!=None:
            if cur.aNum == aNum:
                return True
            else:
                cur = cur.next
        return False

    def addElement(self, aNum, name, phone, address):
        if not self.isMember(aNum):
            newNode = self.Node(aNum,name,phone,address)
            index = self.hash(aNum)
            newNode.next = self.hashTable[index]
            self.hashTable[index] = newNode

    def printHashTable(self):
        for i in range(self.tablesize):
            cur = self.hashTable[i]
            print(f'Index {i}: ', end='')
            while cur:
                print(f'({cur.aNum},{cur.name},{cur.phone},{cur.address}) -> ', end='')
                cur = cur.next
            

a = openHash()
a.addElement(1, 'Ali', '123456', 'Lahore')
a.addElement(2, 'Ahmed', '123456', 'Karachi')
a.addElement(3, 'Asad', '123456', 'Islamabad')
a.addElement(4, 'Ali', '123456', 'Lahore')
a.addElement(5, 'Ahmed', '123456', 'Karachi')
print(a.isMember(1))
a.printHashTable()
