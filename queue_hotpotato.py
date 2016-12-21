''' children line up in a circle and pass an item from neighbor to neighbor as
fast as they can. At a certain point in the game, the action is stopped and
the child who has the item (the potato) is removed from the circle. Play
continues until only one child is left. '''

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[len(self.items)-1]

	def __str__(self):
		return str(self.items)


def hotpotato(namelist, num):
	q = Queue()

	for name in namelist:
		q.enqueue(name)

	while q.size() > 1:
		for i in range(num):
			q.enqueue(q.dequeue())

		q.dequeue()

	return q.dequeue()


print hotpotato(["Bill","David","Susan","Jane","Kent","Brad"],7)
