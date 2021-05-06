class Node():
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        # inserts a Node(val) to the start of the list
        
        node = Node(val)
        if self.head == None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node

    def remove(self):
        # removes and returns first Node. If list is empty, return None

        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def printList(self):
        #prints list

        temp = self.head
        print("Head ->", end = " ")
        while temp is not None:
            print(temp.val, " -> ", end = ' ')
            temp = temp.next
        print('None')

    def getSize(self):
        # gets number of nodes in list

        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print('Total node in list:', count)
    
    def getLastNode(self):
        # gets last node val in list

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        print("Last node value:", temp.val)
    
if __name__ == "__main__":
    newList = LinkedList()
    newList.printList()
    newList.insert(13)
    newList.insert(4)
    newList.insert(23)
    newList.printList()
    newList.remove()
    newList.printList()
    newList.getSize()
    newList.getLastNode()