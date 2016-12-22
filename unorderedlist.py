'''
implementation of ordered and unordered list in python
'''
class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

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
		current = self.head
		while current != None:
			count = count + 1
			current = current.getNext()

		return count

	def search(self, item):
		current = self.head
		found = False
		while current!=None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self, item):
		current = self.head
		found = False
		previous = None
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def append(self, item):
		current = self.head
		found = False
		previous = None
		while not found:
			if current != None:
				previous = current
				current = current.getNext()
			else:
				temp = Node(item)
				previous.setNext(temp)
				found = True


class OrderedList():
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()

		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			previous.setNext(temp)
			temp.setNext(current)

	def size(self):
		count = 0
		current = self.head
		while current != None:
			count = count + 1
			current = current.getNext()

		return count

	def remove(self, item):
		current = self.head
		previous = None
		found = False

		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def search(self, item):
		current = self.head
		previous = None
		stop = False
		found = False

		while not stop and current != None and not found:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()

		return found



mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.append(22)
print "after append"
print(mylist.size())
print(mylist.search(22))


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

