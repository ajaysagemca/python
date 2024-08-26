import random
cnumber=random.randrange(1,101)
userinput=int(input('enter the value:-'))
if cnumber>userinput:
    print("computer number",cnumber)
    print('guessing number is too high')
elif cnumber<userinput:
    print('computer number',cnumber)
    print('guesse=ing number is too low')
else:
    print('computer number',cnumber)
    print("guessing number is equal")

