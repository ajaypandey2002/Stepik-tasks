n = int(input())
for i in range(1, n + 1):
    for j in range(i - 1, -i, - 1):
        print(i - abs(j), sep = '', end='')
    print()