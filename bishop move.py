'''You are given two different cells of the chessboard. Write
 a program that determines whether the bishop can get
 from the first cell to the second in one move. The program receives as input 
four numbers from 1 to 8 each, specifying the column number and line number,
 first for the first cell, then for the second cell. The program should output 
"YES" if the bishop moves from the first cell to the second one, or "NO" otherwise.'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):    
    print('YES')
else:
    print('NO')