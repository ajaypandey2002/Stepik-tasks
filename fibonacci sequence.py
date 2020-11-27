#printing the first n Fibonacci numbers
n = int(input())
x = 0
a = 0
b = 0
for i in range(1, n+1):
    if i<=2: 
        x=1 
        a=1 
        b=1;
        print(x, end = ' ')
    elif i>2: 
        x=a+b 
        a=b 
        b=x
        print(x, end = ' ')