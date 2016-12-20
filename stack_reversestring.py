'''
Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
'''


class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

# my first solution O(N)
def revstring1(mystr):
	s = Stack()
	res = ""
	for i in range(len(mystr)):
		s.push(mystr[i])
	while not s.isEmpty():
		res = res + s.pop() 
	return res	

# is there a better way to do this?
# yes pythonic way
print 'vinod'[::-1]


result = revstring1("vinod")

print result


