print("code 1 bubble_sort")
array = [66, 32, 43, 55, 11]
length = len(array)

def bubble_sort(array, length):
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            print(f"pass no:- {i + 1} - {array}")
    return array

print("initial array", array)
print("sorted array", bubble_sort(array, length))




print()
print("code 2 binary_search")
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 38
result = binary_search(arr, target)
if result != -1:
    print(f"{target} is a target and {result} is index number")
else:
    print("element not found")




print()
print("code 3 linear_search")
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50, 60, 70]
target = 40
result = linear_search(arr, target)
if result != -1:
    print(f"{target} is target that is on {result} index")
else:
    print("not found element")


print()
print("code 4 linear_search using while loop")
def linear_search(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i = i + 1
    return -1

arr = [10, 60, 30, 70, 50, 80, 40]
target = 40
result = linear_search(arr, target)
if result != -1:
    print(f"{target} is target that is on {result} index")
else:
    print("not found element")