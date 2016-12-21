# O(n^2)

def getstr1(a, b):
	c = ""
	d = ""
	if len(a) == len(b):
		for i in range(len(a)):
			for j in range(len(b)):
				if a[i] == b[j]:
					c = c + b[j]

		if a == c:
			print "given 2 text is anagram"
		else:
			print "not anagram"

	else:
		print "length is not same"


# It is O(nlogn) because we use sort()
def getstr2(a, b):

	s1 = list(a)
	s2 = list(b)

	s1.sort()
	s2.sort()

	pos = 0

	matches = True
	while pos < len(s1) and matches:
		if s1[pos] == s2[pos]:
			matches = True
			pos = pos + 1
		else:
			matches = False

	return matches


# O(n)
def getstr3(a, b):

	total_a = 0
	for i in range(len(a)):
		total_a = total_a + ord(a[i])

	total_b = 0
	for j in range(len(b)):
		total_b = total_b + ord(b[j])

	if total_b == total_a:
		print "it is anagram"
	else:
		print "not anagram"

''' 
Given two strings, a and b, that may or may not be of the same length,
determine the minimum number of character deletions required to make them
anagrams. Any characters can be deleted from either of the strings 

e.g. str1 : cde
	 str2 : abc

	 result : 4

'''

def minanagram(a, b):

	c1 = [0]*26
	c2 = [0]*26

	for i in range(len(a)):
		pos = ord(a[i]) - ord('a')
		c1[pos] = c1[pos] + 1

	for i in range(len(b)):
		pos = ord(b[i]) - ord('a')
		c2[pos] = c2[pos] + 1

	j=0
	count = 0
	print c1
	print c2
	while j<26:
		count = count + abs(c1[j]-c2[j])
		j = j + 1

	return count 


print minanagram('cdef','abc')

getstr1("python","typhon")
print(getstr2("python","typhon"))
getstr3("typhon","python")

