print("code 0 REVERSE THE WORD OF STRING")
l=("my name is ajay sahu")
s=l.split()
rev=s[::-1]
convert_list=tuple(rev)
word=' '.join(convert_list)
print(word)



print()
print("CODE 11 replace function")
l=("Listen")
s=("Silent")
str1=l.replace("","").lower()
str2=s.replace("","").lower()

if sorted(str1)==sorted(str2):
    print(f"{str1} and {str2} both are anagram string")




print()
print("CODE 1 replace function")
a=("hello world")
print(a.replace("j","world"))
print(a.replace("hello","world"))
print(a.replace("h","world"))



print()
print("CODE 1FIND THE VOWELS IN STRING")
text=("hello how are you ajay")
vowels=("aeiouAEIOU")
count=0
for i in text:
    if i in vowels:
        count+=1

print("in this string 9 vowels are available =",count)



print()
print("code 2 FIND THE AREA OF CIRCLE")
print()
def math():
    radius = 5
    area = 3.14 * radius * radius
    print("area of circle", area)


print()
print("code 3 FIND THE MAX VALUE OF 3 NUMBER")
'''
math()
a=float(input("enter the 1st value ="))
b=float(input("enter the 2nd value ="))
c=float(input("enter the 3rd value ="))
t=max(a,b,c)
print(t)
'''

print()
print("code 4 PRINT THE TABLE OF 5")
def table():
    x = 5
    for i in range(1, 11):
        print(f"{5} - {5} * {i}= {5 * i}")
table()

print()
print("code 5 FIND THE LCM OF TWO NUMBERS")
a = 12
b = 18
grether = max(a, b)
while True:
    if grether % a == 0 and grether % b == 0:
        lcm = grether
        break
    grether += 1

print(f"the lcm of {a} and {b} is =", lcm)

print()
print("code 6 enumerate")
a=["ajay","sahu","ajju"]
for i,a in enumerate(a,start=1):
    print(i,a)





