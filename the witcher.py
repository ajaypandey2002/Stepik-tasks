#In the world of Witcher has a coins of denomination 1, 5, 10, 25. What's minimum of coins needed for paying to Witcher?
n = int(input())
m25 = 0
m10 = 0
m5 = 0
m1 = 0
while n >= 1:
    if n >= 25:
        m25 += 1
        n -= 25
    elif 10 <= n < 25:
        m10 += 1
        n -= 10
    elif 5 <= n < 10:
        m5 += 1
        n -= 5
    else:
        m1 += 1
        n -= 1
print(m25 + m10 + m5 + m1)