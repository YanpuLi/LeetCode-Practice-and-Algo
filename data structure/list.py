# unordered list 
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
	def getData(self):
		return self.val

	def getNext(self):
		return self.next
	def setData(self, data):
		self.val = data
	def setNext(self, link):
		self.next = link
class UnorderedList:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		return self.head == None
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
	def size(self):
		count = 0
		curr = self.head
		while curr:
			count += 1
			curr = curr.getNext()
		return count
	def search(self, item):
		curr = self.head
		found = False
		while curr and not found:
			if curr.getData() == item:
				found = True
			else:
				curr = curr.getNext()
		return found
	def remove(self, item):
		curr = self.head
		prev = None
		found = False
		while curr and not found:
			if curr.getData() == item:
				found = True
			else:
				prev = curr
				curr = curr.getNext()
		if prev = None:
			self.head = curr.getNext()
		else:
			prev.setNext(curr.getNext())
# ordered List
class orderedList:
	def __init__(self):
		self.head = None
	def search(self, item):
		found = False
		stop = False
		curr = self.head
		while curr != None and not found and not stop:
			if curr.getData() == item:
				found = True
			else:
				if curr.getData() > item:
					stop = True
				else:
					curr = curr.getNext()
		return found
	def add(self, item):
		prev = None
		curr = self.head
		found = False
		while curr != None and not found:
			if curr.getData() > item:
				stop = True
			else:
				prev = curr
				curr = curr.getNext()
		temp = Node(item)
		if prev == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(curr)
			prev.setNext(temp)

