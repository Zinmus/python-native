x = int(input("First number: "))
y = int(input("Second number: "))

def divisors_sum(number):
    suma = 0
    for i in range(1, number):
        if number % i == 0:
            suma += i
    return suma

def are_amicable(x, y):
    if divisors_sum(x) == y and divisors_sum(y) == x:
        return True

if are_amicable(x, y):
    print("These two numbers are amicable.")
else:
    print("These two numbers are not amicable.")
