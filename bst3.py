class BST:
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key
    
    def __init__(self):
        self.root = None
        self.count = 0
        
    def is_empty(self):
        return self.root is None
    
    def getCount(self):
        return self.count
    
    def addNode(self, ele):
        cur = parent = self.root
        while(cur!=None and cur.val!=ele):
            parent = cur
            if ele < cur.val:
                cur = cur.left
            elif ele > cur.val:
                cur = cur.right
        if cur == None:
            newNode = self.Node(ele)
            if parent == None:
                self.root = newNode
            elif ele < parent.val:
                parent.left = newNode
            elif ele > parent.val:
                parent.right = newNode
            self.count += 1
            
    def isMember(self, key):
        if not self.is_empty():
            cur = self.root
            while(cur!=None):
                if key < cur.val:
                    cur = cur.left
                elif key > cur.val:
                    cur = cur.right
                else:
                    break
            return cur != None
        else:
            return False
        
    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            print(node.val, end=' ')
            self.inOrder(node.right)
    
    def preOrder(self,node):
        if node:
            print(node.val, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)
    
    def postOrder(self,node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.val, end=' ')
            
    def deleteNode(self, key):
        if not self.is_empty():
            self.root = self._deleteNode(self.root, key)
    
    def _deleteNode(self, node, key):
        if node == None:
            return node
        if key < node.val:
            node.left = self._deleteNode(node.left, key)
        elif key > node.val:
            node.right = self._deleteNode(node.right, key)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                temp = self._minValueNode(node.right)
                node.val = temp.val
                node.right = self._deleteNode(node.right, temp.val)
        return node
    
    def _minValueNode(self, node):
        if node.left == None:
            return node
        else:
            return self._minValueNode(node.left)


def level_order(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage
bst = BST()
bst.addNode(50)
bst.addNode(30)
bst.addNode(20)
bst.addNode(40)
bst.addNode(70)
bst.inOrder(bst.root)
bst.postOrder(bst.root)