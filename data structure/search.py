#binary search: an ordered list
#method 1 non-recursive
def binarySearch1(l, item):
	first = 0
	last = len(l)-1
	found = False
	while first < last and not found:
		mid = (first + last)//2
		if l[mid] == item:
			found = True
		elif l[mid] < item:
			first = mid+1
		else:
			last = mid -1
	return found
#method 2: recursive
def binarySearch2(l, item):
	if len(l) == 0:
		return False
	mid = len(l)//2
	if item == l[mid]:
		return True
	elif item > l[mid]:
		return binarySearch2(l[mid+1:], item)
	else:
		return binarySearch2(l[:mid-1], item)




#bubble sort, every adjacent comparing
def bubble(l):
	for i in range(len(l)-1):
		for j in range(1, len(l)-i):
			if l[j-1] > l[j]:
				temp = l[j-1]
				l[j-1] = l[j]
				l[j] = temp

#bubble2: if no exchange in one pass, already sorted
def bubble2(l):
	stop = False
	i = 0 
	while i < len(l)-1 and not stop:
		stop = True
		for j in range(1, len(l)-i):
			if l[j-1] > l[j]:
				stop = False
				temp = l[j-1]
				l[j-1] = l[j]
				l[j] = temp
		i = i +1
#selection sort: for each pass, only 1 exchange, move largest to bottom
def selection(l):
	for i in range(len(l)-1, 0 , -1):
		m = 0
		for j in range(1,i+1):
			if l[j] > l[m]:
				m = j
		temp = l[i]
		l[i] = l[m]
		l[m] = temp
#insert sort:
def insert(l):
	for i in range(1, len(1)):
		val = l[i] 
		pos = i
		while pos > 0  and val < l[pos-1]:
				l[pos] = l[pos-1]
				pos = pos -1
		l[pos] = val
#shell sort: modification of insert sort
#using gap to select sublist, use insert sort on sublist, 
#reduce increment, do final sort
def shellSort(l):
	sublistCount = len(l)//2
	while sublistCount >0:
		for startpos in range(sublistCount):
			gapInsertSort(l, startpos, sublistCount):
		print("After increments of size",sublistcount,
                                   "The list is",alist)
		sublistCount = sublistCount//2
def gapInsertSort(l, start, gap):
	for i in range(start+gap, len(l), gap):
		currVal = l[i]
		pos = i 
		while pos >=gap and l[pos] > currVal:
			l[pos] = l[pos-gap]
			pos = pos - gap
		l[pos] = currVal
#merge sort: using extra space
def mergeSort(l):
	if len(l) >1:
		mid = len(l)//2
		left = l[:mid]
		right = l[mid:]
		mergeSort(left)
		mergeSort(right)
		i = 0
		j = 0
		k = 0 
		while i < len(left) and j <len(right):
			if left[i] < right[j]:
				l[k] = left[i]
				i = i+1
			else:
				l[k] = right[j]
				j = j+1
			k = k+1
		while i <len(left):
			l[k] = left[i]
			i = i+1
			k = k+1
		while j <len(right):
			l[k]=right[j]
			j = j+1
			k = k+1
#Quick sort: divide and conquer
#advantage: no extra space
#disad: may not divide into half.
#select a val as pivot value, usually 1st one, split list by pivot value
def quickSort(l, first, last):
	if first < last:
		split = partition(l, first, last)
		quickSort(l, first, split -1)
		quickSort(l, split+1, last)
def partition(l, first, last):
	key = l[first]
	left = 1
	right = len(l)-1
	stop = False
	while not stop:
		while left < right and key > l[left]:
			left = left +1
		while left < right and key < l[right]:
			right = right -1
		if right < left: 
			stop = True
		else:
			temp = l[left]
			l[left] = l[right]
			l[right] = temp
	temp = l[first]
	l[first] = l[right]
	l[right] = temp
	return right

'''
A sequential search is O(n).O(n) for ordered and unordered lists.
A binary search of an ordered list is O(logn).O(log⁡n) in the worst case.
Hash tables can provide constant time searching.
A bubble sort, a selection sort, and an insertion sort are O(n2). O(n2) algorithms.
A shell sort improves on the insertion sort by sorting incremental sublists. It falls between O(n). O(n) and O(n2). O(n2).
A merge sort is O(nlogn)O(nlog⁡n), but requires additional space for the merging process.
A quick sort is O(nlogn)O(nlog⁡n), but may degrade to O(n2)O(n2) if the split points are not near the middle of the list. It does not require additional space.
'''








