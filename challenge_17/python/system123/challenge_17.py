import numpy as np 

# Recursive solutions O(2^n)
def make_change(cash, coins=[25,10,5,1]):
	if cash == 0:
		return(1)
	elif len(coins) == 0 or cash < 0:
		return(0)
	else:
		return(make_change(cash, coins[1:]) + make_change(cash - coins[0], coins))

# This solution uses dynamic programming and O(N) space
def make_change_dp(n, coins=[1,5,10,25]):
	arr = np.zeros(n+1, dtype=int)

	arr[0] = 1

	for i in coins:
		for j in range(i, n+1):
			arr[j] += arr[j - i]

	return(arr[n])

if __name__ == "__main__":
	cnt = make_change_dp(100)
	print(cnt)
