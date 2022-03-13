
import random
l=['stone', 'paper', 'scissors']
pc=0
person=0
j=int(input('chand bar bazi konim? '))
while True:
    x=random.choice(l)
    choose=input('pleaz enter your choose: ')
    if choose == x:
        print('equal')
    elif choose=='stone' and x=='scissors':
        print('you wine')
        person+=1
    elif choose=='paper' and x=='stone':
        print('you wine')
        person+=1
    elif choose=='scissors' and x=='paper':
        print('you wine')
        person+=1
    else:
        print('pc wine')
        pc+=1
    print(f'pc {pc} you {person}')
    if pc==j or person==j:
        break
