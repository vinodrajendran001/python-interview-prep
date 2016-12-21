'''
Left array rotation
d = 4 
[1 2 3 4 5] -> [2 3 4 5 1] -> [3 4 5 1 2] -> [4 5 1 2 3] -> [5 1 2 3 4]
'''

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self, item):
		return self.items.pop(item)

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def __str__(self):
		return str(self.items)


def rotation(n, a):
	s = Stack()
	count = 0
	for i in range(len(a)):
		s.push(a[i])
	while count < n:
		top = s.pop(0)
		s.push(top)
		count = count + 1

	return s


print rotation(3,'12345')