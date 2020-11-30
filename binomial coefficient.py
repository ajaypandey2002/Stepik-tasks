def factorial(n):
	count = 1
	for i in range(1, n + 1):
		count *= i
	return count


def compute_binom(n, k):
	return (factorial(n))//((factorial(k))*(factorial(n-k)))

print(compute_binom(10, 5))

