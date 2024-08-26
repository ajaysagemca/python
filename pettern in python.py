print('first pettern')
x=4
for a in range(1,x+1):
    for b in range(1,a+1):
        print('*',end="")
    print()

print()
print('2nd pettern')
x=4
y=1
for a in range(1,x+1):
    for b in range(1,y+1):
        print("*",end="")
    y=y+2
    print()

print()
print('3rd pettern')
x=4
y=7
for a in range(1,x+1):
    for b in range(1,y+1):
        print("*",end="")
    y=y-2
    print()

print()
print('4th pettern')
x=4
y=4
for a in range(1,x+1):
    for b in range(1,y+1):
        print(" ",end="")
    for c in range(1,a+1):
        print("* ",end="")
    y=y-1
    print()

print()
print('5th pettern')
x=4
y=4
for a in range(1,x+1):
    for b in range(1,y+1):
        print(" ",end="")
    for c in range(1,a+1):
        print("*",end="")
    y=y-1
    print()

print()
print('6th pettern')
x=4
y=0
for a in range(x,0,-1):
    for b in range(0,y+1):
        print(" ",end="")
    for c in range(1,a+1):
        print("* ",end="")
    y=y+1
    print()

print()
print('7th pettern')
x=4
for a in range(1,x+1):
    for c in range(1,a+1):
        print(c," ",end="")
    print()

print()
print('8th pettern')
x=5
for a in range(x,0,-1):
    for c in range(1,a):
        print(c," ",end="")
    print()

print()
print('9th pettern')
x=5
number=1
for a in range(1,x+1):
    for b in range(1,a+1):
        print(number,' ',end="")
        number=number+1
    print()

print()
print('10th pettern')
x=5
for a in range(1,x+1):
    for b in range(1,a+1):
        sum=a+b
        if sum%2==0:
            print('1 ',end="")
        else:
            print('0 ',end="")
    print()

print()
print('11th pettern')
x=5
for a in range(1,x+1):
    space=2*(x-a)
    for b in range(1,a+1):
        print("*",end="")
    for b in range(space):
        print(" ",end="")
    for b in range(1,a+1):
        print("*",end="")
    print()
for a in range(x,-1,-1):
    space=2*(x-a)
    for b in range(1,a+1):
        print("*",end="")
    for b in range(space):
        print(" ",end="")
    for b in range(1,a+1):
        print("*",end="")
    print()

print()
print('12th pettern')
x=5
y=5
for a in range(1,x+1):
    for b in range(1,y+1-a):
        print(' ',end="")
    for b in range(a,0,-1):
        print(b,end="")
    for b in range(2,a+1):
        print(b,end="")
    print()

print()
print('13th pettern')
x=4
y=4
for a in range(1,x+1):
    for b in range(1,y+1-a):
        print(' ',end="")
    for b in range(a,0,-1):
        print("*",end="")
    for b in range(2,a+1):
        print("*",end="")
    print()

print()
print('14th pettern')
x=5
y=4
for a in range(1,x+1):
    for b in range(y+1-a,0,-1):
        print(" ",end="")
    for b in range(1,x+1):
        print("*",end="")
    print()

print()
print('15th pettern')
x=4
y=6
for a in range(1,x+1):
    for b in range(1,y+1):
        if(a==1 or a==x or b==1 or b==y):
            print("*",end="")
        else:
            print(" ",end="")
    print()

print()
print('16th pettern')
x=5
y=4
for a in range(1,x+1):
    for b in range(y+1-a,0,-1):
        print(" ",end="")
    for b in range(1,a+1):
        print(a,"",end="")
    print()

print()
print('17th pettern')
x=4
y=3
for a in range(1,x+1):
    for b in range(1,y+1):
        print(" ",end="")
    for b in range(1,a+1):
        print("* ",end="")
    y=y-1
    print()
p=3
q=3
r=3
for i in range(1,p+1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(1,r+1):
        print("* ",end="")
    r=r-1
    print()

print()
print('18th pettern')

for row in range(5):
    for col in range(5):
        if row+col==2 or col-row==2 or row-col==2 or row+col==6:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print()
print('19th pettern')
for row in range(1,5):
    for col in range(1,8):
        if row==4 or row+col==5 or col-row==3:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print()
print('20 pettern')
n=int(input('enter the row:-'))
for row in range(1,n+1):
    for col in range(1,2*n):
        if row==n or row+col==n+1 or col-row==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print()
print('21 pettern')
n=int(input('enter the row:-'))
k=2
for row in range(1,n+1):
    for col in range(1,2*n):
        if row+col==n+1 or col-row==n-1:
            print("*",end="")
        elif row==n and col!=k:
            print("*",end="")
            k=k+2
        else:
            print(" ",end="")
    print()

print()
print('22th pettern')
k=2
for row in range(1,5+1):
    for col in range(1,9+1):
        if   row+col==6 or col-row==4:
            print("*",end="")
        elif row==5 and col!=k:
            print("*",end="")
            k=k+2
        else:
            print(" ",end="")
    print()



print()
print('23 pettern')
#n=5
for a in range(5,0,-1):
    for b in range(1,a+1):
        if a==5 or a==1 or b==1 or b==a:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print()
print('24 pettern')










