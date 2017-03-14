# remove duplicates in unordered list
def removeDup(l):
    if l.head == None or l.head.next == None:
        return l.head
    curr = l.head
    values = set([curr.val])
    while curr.next:
        if curr.next.val in values:
            curr.next = curr.next.next
        else:
            values.add(curr.next.val)
            curr = curr.next
    return l
# no other buffer allowed
def removeDup2(l):
    if l.head == None or l.head.next == None:
        return l.head
    curr = l.head
    while curr:
        pointer = curr
        while pointer.next:
            if curr.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        curr = curr.next
    return l
from LinkedList import UnorderList
ll = UnorderList()
ll.add(5)
ll.add(4)
ll.add(3)
ll.add(2)
ll.add(2)
ll.add(1)
ll.add(2)
ll.printList()
removeDup(ll)
ll.printList()