'''Two integers mm and nn are given.
Write a program that prints all numbers from mm to nn, inclusive, in ascending order,
if m <nm <n, or in descending order otherwise.'''
m = int(input())
n = int(input())
if m < n:
    for i in range(m, n+1):
        print(i)
else:
    for i in range(m, n-1, -1):
        print(i)