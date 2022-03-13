
from cmath import nan
l=[nan]
row=int(input('choose row: '))
x=(l*row)*2
for j in range(row):
    x[row-j]='*'
    x[row+j]='*'
    for i in x:
        if i=='*':
            print(i,end='')

        else:
            print('',end=' ')
    print()

for j in range(row):
    x[(row*2)-(1+j)]=nan
    x[j+1]=nan
    for i in x:
        if i=='*':
            print(i,end='')

        else:
            print('',end=' ')
    print()