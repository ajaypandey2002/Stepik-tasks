#a prime nummbers in segment [a;b]
a = int(input())
b = int(input())
count = 0
for i in range (a, b + 1):
    for j in range (1, i + 1):
        if i%j == 0:
            count += 1
    if count == 2:
        print(j)
    count = 0