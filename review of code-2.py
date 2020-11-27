#You need to write a program that prints the sum of all negative numbers in the sequence and the maximum negative number in the sequence.
mx = -(10**6) - 1
s = 0
for i in range(1, 11):
    x = int(input())
    if x < 0:
        s += x
    if mx < x < 0:
        mx = x
if mx != -(10**6) - 1:
	print(s)
	print(mx)
else:
	print('NO')