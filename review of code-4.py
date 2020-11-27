#A natural number is received for processing. You need to write a program that displays the maximum digit of a number multiple of 33
n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if max_digit < digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)