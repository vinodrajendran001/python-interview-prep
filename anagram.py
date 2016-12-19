# O(n^2)

def getstr1(a, b):
	c = ""
	d = ""
	if len(a) == len(b):
		for i in range(len(a)):
			for j in range(len(b)):
				if a[i] == b[j]:
					c = c + b[j]
					print c

		if a == c:
			print "given 2 text is anagram"
		else:
			print "not anagram"

	else:
		print "length is not same"


# It is still O(n^2) because we use sort()
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
	print total_a

	total_b = 0
	for j in range(len(b)):
		total_b = total_b + ord(b[j])
	print total_b

	if total_b == total_a:
		print "it is anagram"
	else:
		print "not anagram"



getstr1("python","typhon")
print(getstr2("python","typhon"))
getstr3("typhon","python")