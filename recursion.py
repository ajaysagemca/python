print("normal sum")
def find_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

if __name__ == "__main__":
    print(find_sum(5))


print()
print("sum using recursion")
def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)

# if __name__=="__name__":
print(find_sum(5))

print()
print("fibonacci")


# 0,1,1,2,3,5,8,13
# 0 1 2 3 4 5 6 7
def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(7))

print()
print("factorial using recursion")
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))






