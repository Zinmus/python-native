pi = 3.141592653
newton_sum = 0

def factorial(x):
    if x > 0:
        return x*factorial(x-1)
    return 1

def double_factorial(x):
    if x >= 2:
        return x*double_factorial(x-2)
    return 1

def newton(x):
    global newton_sum
    if 2*newton_sum-pi > 0.0000000001 or pi-newton_sum*2 > 0.0000000001:
        newton_sum += factorial(x)/double_factorial(2*x+1)
        return newton(x+1)
    return x

print(newton(0))

