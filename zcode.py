from math import log,ceil
import math
import sys

log2 = lambda x: log(x,2)



def binary(x,l=1):
	fmt = '{0:0%db}' % l
	return fmt.format(x)

def unary(x):
	return x*'1'+'0'

def elias_generic(lencoding, x):
	if x == 0: return '0'

	l = 1+int(log2(x))
	a = x - 2**(int(log2(x)))

	k = int(log2(x))

	return lencoding(l) + binary(a,k)

def golomb(b, x):
	q = int((x) / b)
	r = int((x) % b)

	l = int(ceil(log2(b)))
	#print q,r,l

	return unary(q) + binary(r, l)


def elias_gamma(x):
	return elias_generic(unary, x)

def elias_delta(x):
	return elias_generic(elias_gamma,x)

def minimal_binary_code(x, z):
	# x in [0,z-1]
	# s = log2(z) upper limit
	# print 'Minimal_binary_code results'
	
	s = int(math.ceil(log2(z)))
	# print 's is: ',s
	# x<2^s-z duadiki leksi

	if x < (math.pow(2,s)) - z:
		result = str(binary(int(x),s-1))
		# print 'Result is: ', result
	else:
		result = int(x - z + math.pow(2,s))
		# print 'Result is: ', result
		result = str(binary(result,s))
		# print 'Result is in binary: ', result

	# print 'Minimal_binary_code RETURN'
	return result

def z_code(x, k):
	#shrinking factor k
	#paremeter

	h = 1
	while True:
		if x < math.pow(2,h*k):
			# print 'There is no z_coding for x = ',x
			# print 'when k = ',k
			return 0
		if (x >= math.pow(2,h*k)) & (x <= math.pow(2,(h+1)*k) - 1 ):
			# print 'X TO ENCODE IS: ', x
			# print 'k is: ', k
			# print 'h is: ', h
			# print 'Bot limit: ', math.pow(2,h*k)
			# print 'Top limit: ', math.pow(2,(h+1)*k) - 1
			firstEl = unary(h+1)
			y = x - math.pow(2,h*k)
			z = math.pow(2,(h+1)*k) - math.pow(2,h*k) - 1
			# print 'x var is: ', y
			# print 'z var is: ', z
			secondEl = minimal_binary_code(y, z)
			return firstEl + secondEl
		else:
			h+=1

#askisi 4
for j in range(1,16):
	for i in range(1,5):
		res = z_code(j, i)
		if res != 0:
			print "x={} ,k={}, z_code={}".format(j,i,res)
