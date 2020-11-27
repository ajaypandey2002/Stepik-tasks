n = int(input())
for i in range(1, n//2 + 2):
    print('*'*i)
for i in range(1, n//2 + 1):
    print('*'*((n//2 + 1) - i))