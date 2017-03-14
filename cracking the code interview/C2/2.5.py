from LinkedList import UnorderList
def sum_list(l1, l2):
	if l1 == None:
		return l2
	if l2 == None:
		return l1
	ll = new UnorderList()
	carry = 0
	h1, h2 = l1.head, l2.head
	while h1 or h2:
		result = carry
		if h1:
			result += h1.val
			h1 = h1.next
		if h2:
			result += h2.val
			h2 = h2.next
		ll.add(result%10)
		carry = result //10
	if carry:
		ll.add(carry)
	return ll