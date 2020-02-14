def calc_factorial(x):
    if x == 1:
        return 1
    return (x * calc_factorial(x-1))

num = 4
#print("the factorial of ", num, "is", calc_factorial(num))

def factorial_calculation(x):
    if x == 1:
        return 1
    else:
        return (x * factorial_calculation(x-1))
print(factorial_calculation(4))