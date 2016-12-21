'''
convert decimal no to binary, oct, hexa
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

	def __str__(self):
		return str(self.items)


def divideby2(decimalNo):

	s = Stack()
	res = ""
	while decimalNo > 0:
		rem = decimalNo % 2
		s.push(rem)
		decimalNo = decimalNo / 2

	while not s.isEmpty():
		res = res + str(s.pop())

	return res


def baseconverter(decimalNo, base):

	s = Stack()
	res = ""
	digits = '0123456789ABCDEF'
	while decimalNo > 0:
		rem = decimalNo % base
		s.push(rem)
		decimalNo = decimalNo / base

	while not s.isEmpty():
		res = res + digits[s.pop()]

	return res


print baseconverter(26, 26)


		