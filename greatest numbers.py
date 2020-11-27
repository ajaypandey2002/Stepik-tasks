n = int(input())
k = 0
l = 0  #the greatest number
pl = -1  #the second greatest number
for i in range(1, n+1):
    k = int(input())
    if k >= l:
        pl = l
        l = k
    elif (k < l) and (k > pl):
        pl = k
print(l)
print(pl)