print("code 1 palindrom")
s=input('enter the value:-')
rev=(s[::-1])
if rev==s:
    print("palindrom")
else:
    print("not palindrom")


print()
print("code 2 is_armstrong ")
def is_armstrong(num):
    sum = 0
    temp = num
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10
    return sum == num

num = 153
if is_armstrong(num):
    print(f"{num} is an armstrong")
else:
    print(f"{num} is not an armstrong")




