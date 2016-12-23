'''
Calculating the Sum of a List of Numbers using Recursion
'''

def listsum(numbers):
	if len(numbers) == 1:
		return numbers[0]
	else:
		return numbers[0] + listsum(numbers[1:])


'''
Factorial using recursion
'''
def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)

'''
Converting an integer to a string in any base
'''
def toStr(n, base):
	convString = "0123456789"
	if n < base:
		return convString[n]
	else:
		return toStr(n/base, base) + convString[n%base] 

'''
Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
'''
def revStr(inpstr):
	if len(inpstr) == 1:
		return inpstr[0]
	else:
		return revStr(inpstr[1:]) + inpstr[0]



'''
Stack frames implementing recursion
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


def toStrstack(n, base):
	convString = "0123456789ABCDEF"
	res = ""
	s = Stack()
	while n > 0:
		if n < base:
			s.push(convString[n])
		else:
			s.push(convString[n%base])
		n = n / base

	while not s.isEmpty():
		res = res + str(s.pop())

	return res

print listsum([1,3,5,7,9])
print fact(3)
print toStr(10,2)
print revStr("vinod")


# to check palindrome or not

inp = "vinod"
rev = revStr(inp)
if inp == rev:
	print "palindrome"
else:
	print "not palindrome"




print toStrstack(1453,16)