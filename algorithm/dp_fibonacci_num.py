def fibonacci(num):
	memo = {}
	for i in range(1, num+1):
		if i <= 2:
			memo[i] = 1
		else:
			memo[i] = memo[i-1] + memo[i-2]
	return memo
def new_fibonacci(num):
	memo = {}
	if num in memo:
		return memo[num]
	if num <= 2:
		memo[num] = 1
	else:
		memo[num] = new_fibonacci(num-1) + new_fibonacci(num-2)
	return memo[num]
print(fibonacci(10))
print(new_fibonacci(10))
