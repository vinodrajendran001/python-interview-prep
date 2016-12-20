'''
Simple Balanced Parentheses using stack
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

# function to check only "(" paranthesis
def paranCheck(paranthesis):
	s = Stack()
	index = 0
	balanced = True
	while index < len(paranthesis) and balanced:
		if(paranthesis[index] == '('):
			s.push(paranthesis[index])
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

# function to check all paranthesis

def genparanCheck(paranthesis):
	s = Stack()
	index = 0
	balanced = True
	while index < len(paranthesis) and balanced:
		if paranthesis[index] in "([{":
			s.push(paranthesis[index])
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, paranthesis[index]):
					balanced = False
		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

def matches(open,close):
	opens = "([{"
	closers = ")]}"
	print "open:", opens.index(open)
	print "close:", closers.index(close)
	return opens.index(open) == closers.index(close)
			
print genparanCheck('({})')