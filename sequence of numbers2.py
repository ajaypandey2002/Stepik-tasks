'''Two integers mm and nn (m> nm> n) are given. Write a program that 
prints all odd numbers from mm to nn, inclusive, in descending order.m = int(input())'''
n = int(input())
if m%2 != 0:
    for i in range(m, n-1, -2):
        print(i)
else:
    for i in range(m-1, n-1, -2):
        print(i)
