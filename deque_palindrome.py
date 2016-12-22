'''
A palindrome is a string that reads the same forward and backward, for example, radar, toot, and madam.
'''

class Deque:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)


def palindrom(inpstr):
	d = Deque()
	palindrome = True
	for i in range(len(inpstr)):
		d.addRear(inpstr[i])

	while d.size() > 1 and palindrome:
		first = d.removeRear()
		last = d.removeFront()
		if first != last:
			palindrome = False

	return palindrome

print palindrom("madam")