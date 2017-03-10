#if p2.val < x, then move p2 to the left side of head
def partition(l , x):
    if l.head == None:
        return None
    p1 = l.head
    p2 = l.head.next
    while p2 != None:
        if p2.val <x:
            p1.next = p2.next
            p2.next = l.head
            l.head = p2
            p2 = p1.next
        else:
            p1 = p1.next
            p2 = p2.next