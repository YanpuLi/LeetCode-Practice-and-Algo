from LinkedList import UnorderList

def is_palindrome(ll):
	fast, slow = ll.head, ll.head
	stack = []
	while fast and fast.next:
		stack.append(slow.val)
		slow = slow.next
		fast = fast.next.next
	if fast:
		slow = slow.next
	while slow:
		top = stack.pop()
		if top != slow.val:
			return False
		slow = slow.next
	return True


