def moveTower(height, fromPole, toPole, withPole):
	if height >= 1:
		print height, fromPole, toPole, withPole
		moveTower(height-1, fromPole, withPole, toPole)
		print height, fromPole, toPole, withPole
		movePole(fromPole, toPole)
		moveTower(height-1, withPole, toPole, fromPole)
		print height, fromPole, toPole, withPole



def movePole(fp, tp):
	print "moving disk from", fp, "to", tp


moveTower(3, "A", "B", "C")


