#https://code.google.com/codejam/contest/6224486/dashboard#s=p1

BASELIMIT = 3

def basecase(p):

	for i in xrange(len(p)):
		if p[i] > BASELIMIT: return False

	return True

def split(p):
	maxp = p[0]
	index = 0

	for i in xrange(len(p)):
		if p[i] > maxp:
			maxp = p[i]
			index = i

	del p[index]
	h1 = maxp / 2
	h2 = maxp - h1
	p.append(h1)
	p.append(h2)

def minmin(diners, pancakes):
	p = pancakes.split(' ')
	t = 0
	mint = 0

	for i in xrange(len(p)):
		p[i] = int(p[i])

	mint = max(p)
	while basecase(p) == False:
		maxp = max(p)
		if t + maxp < mint: mint = t + maxp
		split(p)
		t += 1

	maxp = max(p)
	if t + maxp < mint: mint = t + maxp

	return mint


#main

cases = raw_input()
output = []

for i in xrange(int(cases)):
	diners = raw_input()
	pancakes = raw_input()
	output.append(minmin(int(diners), pancakes))
	# print pancakes
	# print 'Case #' + str(i+1) + ":", output[i]

for i in xrange(len(output)):
	print 'Case #' + str(i+1) + ":", output[i]