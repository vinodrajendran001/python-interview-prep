# function to determine minimum no. in a  list with O(n^2)
def findmin(alist):
	overallmin = alist[0]
	for i in alist:
		isoverallmin = True
		for j in alist:
			if i > j:
				isoverallmin = False
		if isoverallmin:
			overallmin = i

	return overallmin


# function to determine minimum no. in a  list with O(n)
def linearfindmin(alist):
	overallmin = alist[0]
	for i in alist:
		if i < overallmin:
			overallmin = i

	return overallmin

print(findmin([5,4,3,2,1]))
print(linearfindmin([1,4,3,2,5]))