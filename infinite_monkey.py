# -*- coding: utf-8 -*-
'''
Here’s a self check that really covers everything so far. You may have
heard of the infinite monkey theorem? The theorem states that a monkey hitting
keys at random on a typewriter keyboard for an infinite amount of time will
almost surely type a given text, such as the complete works of William
Shakespeare. Well, suppose we replace a monkey with a Python function. How
long do you think it would take for a Python function to generate just one
sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like
a weasel”

You’re not going to want to run this one in the browser, so fire up your
favorite Python IDE. The way we’ll simulate this is to write a function that
generates a string that is 27 characters long by choosing random letters from
the 26 letters in the alphabet plus the space. We’ll write another function
that will score each generated string by comparing the randomly generated
string to the goal.

A third function will repeatedly call generate and score, then if 100% of the
letters are correct we are done. If the letters are not correct then we will
generate a whole new string.To make it easier to follow your program’s
progress this third function should print out the best string generated so far
and its score every 1000 tries. 
'''
import random

def generatorSen(strlen):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	res = ""
	for i in range(strlen):
		res = res + alphabet[random.randrange(strlen-1)]

	return res

def score(goalstr, teststr):
	numScore = 0
	for i in range(len(goalstr)):
		if goalstr[i] == teststr[i]:
			numScore = numScore + 1

	return numScore/float(len(goalstr))

def main():
	goalstr = "methinks it is like a weasel"
	newstr = generatorSen(28)
	best = 0
	newscore = score(goalstr, newstr)
	while newscore < 1:
		if newscore > best:
			print newscore, newstr
			best = newstr
		newstr = generatorSen(28)
		newscore = score(goalstr, newstr)

main()

