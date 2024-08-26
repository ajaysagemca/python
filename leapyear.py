year=int(input('enter the leap year:-'))

if(year%400==0) and (year%100==0):
    print(year,'leap year')

elif(year%4==0) and (year%100!=0):
    print(year,'leap year')

else:
    print(year,'not leap year')
