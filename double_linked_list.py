class Node():
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Double_LL():
    def __init__(self, head = None):
        self.head = None
        self.tail = self.head

    def addNodeLast(self,val):
        node = Node(val)
        if self.head == None:
            # if no node in list
            node.right = None
            self.head = node
            self.tail = node
        else:
            temp = self.head
            while temp.right is not None:
                temp = temp.right
            temp.right = node
            node.left = temp
            self.tail = node
    
    def addNodeStart(self,val):
        node = Node(val)
        if self.head == None:
            node.right = None
            self.head = node
            self.tail = node
        else:
            node.right = self.head
            self.head = node
    
    def addNodeAtIndex(self, index, val):
        if index >= self._size():
            raise IndexError("index out of range")
        temp = self.head
        while index > 0:
            temp = temp.right
            index -= 1
        node = Node(val)
        node.left = temp.left
        temp.left.right = node
        node.right = temp
        temp.left = node
            
    
    def printList(self):
        temp = self.head
        print('Head ->', end = ' ')
        while temp is not None:
            print(temp.val, ' -> ', end = ' ')
            temp = temp.right
        print('None')

    def getSize(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.right
        print('Total node in list:', count)
    
    def _size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.right
        return count

if __name__ == "__main__":
    newDLL = Double_LL()
    newDLL.addNodeLast(2)
    newDLL.addNodeLast(5)
    newDLL.addNodeLast(8)
    newDLL.printList()
    newDLL.addNodeStart(4)
    newDLL.printList()
    print(newDLL.tail.val)
    print(newDLL.head.val)
    newDLL.addNodeAtIndex(2,88)
    newDLL.printList()
    newDLL.addNodeAtIndex(9,88)