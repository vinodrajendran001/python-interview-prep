class Stack:
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def __str__(self):
		return str(self.items)

def unsortedseqSearch(alist, item):
	if alist[0] == item:
		return True
	else:
		if len(alist) <= 1:
			return False
		else:
			return unsortedseqSearch(alist[1:], item)

print unsortedseqSearch([1,2,3,4,5],6)

s = Stack()

def sortedseqSearch(alist, item):
	s.push(alist)
	if alist[0] == item:
		return True
	elif alist[0] > item or len(alist) <= 1:
		return False
	else:
		return sortedseqSearch(alist[1:], item)


print sortedseqSearch([1,2,4,5,6,7,8,9],3)
print s
