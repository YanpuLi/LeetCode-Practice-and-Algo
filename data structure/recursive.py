'''
dynamic programming
optimization of making changes, 1 cent, 5 cent, 1 dime, 1 quater
method 1 and method 2 are not dynamic programming
method 1, greedy method
'''very inefficient, because for the same path, need to be recaculated many times
def recDC(coinList, change):
	minCoins = change
	if change in coinList:
		return 1
	else:
		for i in [ c for c in coinList if c <= change]:
			numCoins = 1 + recDC(coinList, change - i)
			if numCoins < minCoins:
				minCoins = numCoins
	return minCoins
print(recMC([1,5,10,25],63))

#use a table to record known path
def recDC2(coinList, change, path):
	minCoins = change
	if change in coinList:
		path[change] = 1
		return 1
	elif path[change] >0:
		return path[change]
	else:
		for i in [c for c in coinList if c <= change]:
			numCoins = 1+ recDC2(coinList, change -i, path)
			if numCoins < minCoins:
				minCoins = numCoins
				path[change] = minCoins

	return minCoins, path
# method 3, dynamic programming
#start with making change for one cent and systematically work its way up to the amount of change we require. 
#This guarantees us that at each step of the algorithm we already know the minimum number of coins needed to make change for any smaller amount.
#disadvantage do not keep track of the coins we use
def dpMakeChange(coinList, change, minCoins):
	for cents in range(change+1):
		coinCount = cents
		for j in [c for c in coinList if c <= cents]:
			if minCoins[cents -j] +1 < coinCount:
				coinCount = minCoins[cents -j] +1 
		minCoins[cents] = coinCount
	return minCoins[change]

#method 4 
# can easily extend dpMakeChange to keep track of the coins used by simply remembering the last coin we add for each entry in the minCoins table
def dpMakeChange2(coinList, change, minCoins, coinUsed):
	for cents in range(change+1):
		coinCount = cents
		newCoin = 1
		for j in [ c for c in coinList if c<= cents]:
			if minCoins[cents-j] +1 < coinCount:
				coinCount = minCoins[cents-j]+1
				newCoin = j
		minCoins[cents] = coinCount
		coinUsed[cents] = newCoin
	return minCoins[change]
def printCoins(coinUsed, change):
	coin = change
	while  coin >0:
		thisCoin = coinUsed[coin]
		print thisCoin
		coin = coin - thisCoin
def main():
	amount = 63
	clist = [1,5,10,21,25]
	coinUsed = [0]*(amount+1)
	coinCount = [0]*(amount+1)
	print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)
main()






