a=[1,4,9,16,25,36,49,64,81,100]
i=0
x=16
while i<len(a):
    if(a[i]==x):
        print('found',i)
        i=i+1
        continue
    else:
        print('nor found',i)
    i=i+1

print('continue')

i=0
while(i<5):
    if(i==3):
        i=i+1
        continue
    print(i)
    i=i+1