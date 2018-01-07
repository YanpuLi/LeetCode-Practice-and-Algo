class queue:
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.insert(0, item)
	def dequeue(self):
		self.items.pop()
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)
# simulate printer
import random
class Printer:
	def __init__(self, ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0
	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining -1
			if self.timeRemaining <=0:
				self.currentTask = None
	def busy(self):
		if self.currentTask != None:
			return True
		return False
	def startNext(self, newTask):
		self.currentTask = newTask
		self.timeRemaining = newTask.getPages()*60/self.pagerate
class Task:
	def __init__(self, time):
		self.timeStamp = time
		self.pages = random.randrange(1,21)
	def getStamp(self):
		return self.timeStamp
	def getPages(self):
		return self.pages
	def waitTime(self, currentTime):
		return currentTime - self.timeStamp

def newPrintTask():
	num = random.randrange(1, 181)
	if num == 180:
		return True
	return False
def simulator(numSeconds, pagesPerMinute):
	printer = Printer(pagesPerMinute)
	printQ = queue()
	waitingtime = []
	for currentSecond in range(numSeconds):
		if newPrintTask():
			task = Task(currentSecond)
			printQ.enqueue(task)
		if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append(nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

# deque: double ended queue
class deque:
	def __init__(self):
		self.items = []
		
	def addRear(self, item):
		self.items.insert(0, item)
	def addFront(self, item):
		self.items.append(item)
	def removeRear(self):
		return self.items.pop(0)
	def removeFront(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)
#palindrome checker
def palChecker(s):
	deq = deque()
	



