# https://code.google.com/codejam/contest/6224486/dashboard#s=p0

def min_inv(smax, si):
	standing = 0
	needed = 0
	smax = int(smax)
	p = []

	for i in xrange(len(si)):
		p.append(int(si[i]))

	for i in xrange(len(p)):

		if i > standing and p[i] != 0: 
			needed += i - standing
			standing += i - standing

		standing += p[i]

	return needed


#main
cases = raw_input()
output = []

for i in xrange(int(cases)):
	line = raw_input()
	smax = line.split(' ')[0]
	si = line.split(' ')[1]
	output.append(min_inv(smax, si))

for i in xrange(len(output)):
	print 'Case #' + str(i+1) + ":", output[i]