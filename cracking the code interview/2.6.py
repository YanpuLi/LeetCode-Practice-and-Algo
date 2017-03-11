def find_beginning(l):
	fast, slow = l.head, l.head
	# find the meeting point
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			break
	#check if it is a circular list
	if fast == None or fast.next == None:
		return None
	#find the beginning point
	fast = l.head
	while fast != slow:
		fast = fast.next
		slow = slow.next
	return fast