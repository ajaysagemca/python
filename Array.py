
print("code 0  FIND THE FIRST AND LAST OCCURRENCE")
arr=[1,2,5,5,5,5,123,125]
print("first occurrence =",arr.index(5))
rev=arr[::-1].index(5)
ori=len(arr)-1-rev
print("last occurrence =",ori)



print("code 0  FIND THE FIRST,SECOND AND LAST OCCURRENCE")
arr=[1,2,5,5,5,5,123,125]
first_occurence=arr.index(5)
print("first occurence =",first_occurence)
try:
    second_occurence=arr.index(5,first_occurence+1)
    print("second occurence =",second_occurence)
except ValueError:
    print("5 does not occure second time")
rev=arr[::-1].index(5)
lenth=len(arr)
ori=lenth-1-rev
print("last occurence =",ori)





print()
print("code 1  TRIPLET FOUND")
def triplet():
    A=[1, 2, 3, 4, 6]
    x=10
    n=len(A)
    for i in range(n):
        l=i+1
        k=n-1
        while l<k:
            csum=A[i] + A[l] + A[k]
            if csum==x:
                print(f"TRIPLET FOUND : {A[i]}, {A[l]}, {A[k]} =",csum)
                l+=1
                k-=1
            elif l<k:
                l+=1
            else:
                k-=1
triplet()


print()
print("code 2 TRIPLET FOUND")
def triplet1():
    A = [20, 22, 24, 28, 26]
    x = 70
    n = len(A)
    for i in range(n):
        l = i + 1
        k = n - 2
        while l < k:
            csum = A[i] + A[l] + A[k]
            if csum == x:
                print(F"TRIPLET FOUND : {A[i]}, {A[l]}  {A[k]} = ", csum)
                l += 2
                k -= 2
            elif csum < x:
                l += 2
            else:
                l -= 2

triplet1()



print()
print("code 3 FIND THE SMALEST AND LARGEST NUMBER USING INDEX  ")
a=[1,2,4,6,8,9]
n=sorted(a)
smalest_element=n[1]
largest_element=n[-2]
print("smalest element=",smalest_element)
print("largest element=",largest_element)



print()
print("code 4 find the smallest element in array")
rray=[6,4,5,3,2,1]
array=sorted(rray)
smallest=array[0]
for num in array:
    if num<smallest:
        smallest=num

print("smallest element =",smallest)







print()
print("code 5 FIND THE SECOND SMALEST NUMBER USING FOR LOOP AND IF ELSE CONDITION ")
# arr=[1,2,3,4,5,6]
ar = [2, 5, 4, 3, 6, 1]
arr = sorted(ar)
smalest = arr[0]
second_smalest = arr[1]

if smalest > second_smalest:
    smalest = second_smalest
    second_smalest = smalest
elif smalest < second_smalest:
    smalest = second_smalest
    second_smalest = smalest
    print(smalest)
    print(second_smalest)
for num in arr[2:]:
    if num < smalest:
        second_smalest = smalest
        smalest = num
    elif num < second_smalest:
        smalest = second_smalest
        second_smalest = num

print("second_smalest=", second_smalest)




print()
print("code 6 FIND THE SECOND SMALEST AND LARGEST NUMBER USING FOR LOOP AND IF ELSE CONDITION ")
#arr = [1, 2, 3, 4, 5, 6]
arr=[2,5,4,3,6,1]

smallest = arr[0]
second_smallest = arr[1]
largest = arr[0]
second_largest = arr[1]

if smallest > second_smallest:
    smallest, second_smallest = second_smallest, smallest

if largest < second_largest:
    largest, second_largest = second_largest, largest

for num in arr[2:]:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest:
        second_smallest = num

    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

print("second_smallest", second_smallest)
print("second_largest=", second_largest)





print()
print("code 7 find the duplicates elements in array")
array = [6, 4, 5, 3, 2, 1, 3, 2]
arr = sorted(array)
duplicates = []
seen = set()
for num in arr:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)

print("duplicates elements =", duplicates)



print()
print("code 8 find the duplicates and unique elements in array")
array = [6, 4, 5, 3, 2, 1, 3, 2]
arr = sorted(array)
duplicates = []
uniques = []
seen = set()
for num in arr:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)
        uniques.append(num)
print("duplicates elements =", duplicates)
print("uniques elements =", uniques)




print()
print("code 9 find the occurence of string")
def occurence(str1, n, x):
    count = 0
    for i in range(len(str1)):
        if str1[i] == x:
            count += 1
    repitition = n // len(str1)
    count = count * repitition

    l = n % len(str1)
    for j in range(l):
        if str1[j] == x:
            count += 1
    return count

str1 = "abcab"
n = 17
print("occurence of a is =", occurence(str1, n, "a"))



print()
print("code 10 basic hashmap code")
hashmap={
    "name":"ajay",
    "college":"sage",
    "age":22
}
print(hashmap["name"])
hashmap["department"]="IT"
hashmap["position"]="engineer"
print(hashmap)
print(type(hashmap))



print()
print("code 11 find the two sum")
def twosum(num, target):
    hashmap = {}

    for i, num in enumerate(num):
        complement = target - num

        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

    return []
num = [2, 7, 11, 15]
target = 9
print(twosum(num, target))


print()
print("code 12 sum of two numbers without + operator")
a=10
b=20
add=a-(-b)
print("sum of two number is =",add)


print()
print("code 13 sum of two numbers without + operator using sum function")
a=10
b=20
print("sum of two numbers is =",sum([a,b]))

print()
print("code 14 sum of two numbers without + operator using fsum function of math module")
import math
a=10
b=20
result=math.fsum([a,b])
print(result)
print(int(result))

print()
print("code 15 lambda function")
sum1=lambda num: num + 10
addition=sum1(5)
print(addition)



