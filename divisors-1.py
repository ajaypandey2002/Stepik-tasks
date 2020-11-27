#Write a program that finds a natural number from the segment [a; b] with the maximum sum of divisors.
max = 0
sum1 = 0
sum2 = 0
a = int(input())
b = int(input())
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum2 += j
        if sum2 >= sum1:
            sum1 = sum2
            max = i
    sum2 = 0   
print(max, sum1)
                