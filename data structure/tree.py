#using list in list to represent a tree
def binaryTree(r):
	return [r,[],[]]
def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t) >1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root
def insertRight(root, newBranch):
	t = root.pop()
	if len(t) >1:
		root.insert(2, [newBranch, [], t])
	else:
		root.insert(2, [newBranch, [], []])
def getRootVal(root):
	return root[0]
def setRootVal(root, val):
	root[0] = val
def getLeftChild(root):
	return root[1]
def getRightChild(root):
	return root[2]
#define class
class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.left = None
		self.right = None
	def insertLeft(self, newNode):
		if self.left == None:
			sel.left = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.left = self.left
			self.left = t 
	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.right = self.right
			self.right = t
	def getRightChild(self):
		return self.right
	def getLeftChild(self):
		return self.left
	def getRootVal(self):
		return self.key
	def setRootVal(self, val):
		self.key = val
# build a parse tree from a fully parenthesized mathematical expression.
from stack import stack

def buildParseTree(fpexp):
	fl = fpexp.split()
	pStack = stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currTree = eTree
	for i in fl:
		if i == '(':
			currTree.insertLeft('')
			pStack.push(currTree)
			currTree = currTree.getLeftChild()
		elif i not in ['+', '-', '*', '/', ')']:
			currTree.setRootVal(int(i))
			parent = pStack.pop()
			currTree = parent
		elif i in ['+', '-', '*', '/']:
			currTree.setRootVal(i)
			currTree.insertRight('')
			pStack.push(currTree)
			currTree = currTree.getRightChild()
		elif i == ')':
			currTree = pStack.pop()
		else:
			raise ValueError
	return eTree
	