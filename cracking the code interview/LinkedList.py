# unordered
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def getData(self):
        return self.val
    def getNext(self):
        return self.next

class UnorderList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        
    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
        return count
    
    def search(self, item):
        curr = self.head
        while curr != None:
            if curr.val == item:
                return True
            curr = curr.next
        return False
    def remove(self, item):
        prev = None
        curr = self.head
        found = False
        while not found:
            if curr.val ==item:
                found = True
            else:
                prev = curr
                curr = curr.next
        if prev == None:
            self.head = curr.next
        else:
            prev.setNext(curr.next)
    def printList(self):
        node = self.head
        while node != None:
            print node.val
            node = node.next
#ordered
class orderList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        prev = None
        curr = self.head
        stop = False
        while curr != None and not stop:
            if curr.getData() > item:
                stop = True
            else:
                prev = curr
                curr = curr.getNext()
        temp = Node(item)
        temp.setNext(curr)
        if prev == None:
            self.head = temp
        else:
            prev.setNext(temp)
    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            curr = curr.getNext()
            count += 1
        return count
    def search(self, item):
        curr = self.head
        while curr != None:
            if curr.getData() == item:
                return True
            curr = curr.getNext()
        return False
    def remove(self, item):
        prev = None
        curr = self.head
        found = False
        while not found:
            if curr.getData() ==item:
                found = True
            else:
                prev = curr
                curr = curr.getNext()
        if prev == None:
            self.head = curr.getNext()
        else:
            prev.setNext(curr.getNext())

            
def reverseList(head):
    curr = head.next
    head = None
    while curr:
        next, curr.next = curr.next, head
        head, curr = curr, next
    return head
        
    