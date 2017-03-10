'''
the kth element to the last one
1st using recursive method
2nd using iterative method, 2 pointers
'''
def findKth(head, k):
    if head == None:
        return 0
    
    i= findKth(head.next, k)+1
    if i == k:
        print 'The %ith element is %i'%(k, head.val)
    return i
findKth(ll.head, 1)

def findKth2(head, k):
	if head == None:
		return None
	p1, p2 = head, head
	step = k-1
	while step > 0:
		if p2 == None: return None
		p2 = p2.next
		step -= 1
	if p2 == None: return None
	while p2.next != None:
		p1=p1.next
		p2=p2.next
	return p1.val