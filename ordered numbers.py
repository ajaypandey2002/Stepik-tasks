#is the numbers are ordered from left to right
n = int(input())
last = n%10
k = 0
m = 0
while n != 0: 
    if n % 10 >= last:
        last = n % 10
        k += 1
    m += 1
    n = n // 10  
if k == m:
    print('YES')
else:
    print('NO')
