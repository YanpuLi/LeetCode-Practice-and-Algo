def factor(n):
    i = n 
    while i>0:
        if n%i==0:
            print i
        i -= 1
#calculate factorial
def calFact(n):
	if n == 0:
		return 0
	return n*calFact(n-1)