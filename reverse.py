print(round(7.9))
print(round(7.5))
print(round(7.4))
print(round(4.5))
print(round(6.6))
print(round(3.141312,1))
print(round(3.141312,2))
print(round(3.141312,3))
print(round(1234, -1))  # 1230  (10s place tk round)
print(round(5678, -2))  # 5700  (100s place tk round)
print(round(98765, -3)) # 99000 (1000s place tk round)
print(round(5122, -3))
print(round(5))




print()
print('code 1 prime number')
a=int(input('enter the value:-'))
if a<2:
    print('not prime')
else:
    for b in range(2,(a)):
        if a%b==0:
            print('not prime')
            break
    else:
     print('prime')



print()
print("code 2 prime_list")
def prime_list(start, end):
    a = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                a.append(num)
    return a

start = 2
end = 101
print(prime_list(start, end))



print()
print('code 3 reverse number')
a=int(input('enter the value:-'))
rev=0
while a>0:
    rev=(0*10)+a%10
    a=a//10
    print('reverse number is:-',rev)



print()
print(' code 4 factorial')
a=int(input('enter the value:-'))
fac=1
while a>0:
    fac=fac*a
    a=a-1
    print('factorial number is:-',fac)#5,20,60,120,120

print()
print("code 5 print the natural numbers")
n=int(input("enter the natural number ="))
for i in range(1,n+1):
    print(i,end=" ")



print()
print("code 6 check the number is perfect or not")
def is_perfect_number(num):
    sum_of_divisor = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_of_divisor += i
            print(sum_of_divisor, i)
    return sum_of_divisor == num

num = 28
if is_perfect_number(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")





print()
print("code 7 check the perfect square sing sqrt function")
import math
def is_perfect_square(num):
    root = math.sqrt(num)
    return root == int(root)

num = 64
if is_perfect_square(num):
    print(f"{num} is a perfect square ")
else:
    print(f"{num} is not  a perfect square")




print()
print("code 8 check the perfect square or not")
def is_perfect_square(num):
    square = round(num ** (1 / 2))
    return square ** 2 == num

num = 25
if is_perfect_square(num):
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")




print()
print("code 9 check the perfect cube or not")
def is_perfect_cube(num):
    cube = round(num ** (1 / 3))
    return cube ** 3 == num

num = 27
if is_perfect_cube(num):
    print(f"{num} is a perfect cube")
else:
    print(f"{num} is not a perfect cube")








