#if everyone from enter numbers is even then YES
n = 0
k = 0
for i in range(1, 11):
    k = int(input())
    if k%2 == 0:
        n += 1
if n != 10:
    print('NO')
else:
    print('YES')