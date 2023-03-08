numerator = int(input("Give a numerator: "))
denominator = int(input("Give a denominator: "))
numbers_list = []

def are_coprime(x, y):
    max_number = max(x, y)
    for i in range(2, max_number):
        if x % i == 0 and y % i == 0:
            return False
    return True

def main_algorithm(r):
    a = int(r)
    numbers_list.append(a)
    if r - a <= 0.0000000001:
        return
    else:
        return main_algorithm(1 / (r - a))

if are_coprime(numerator, denominator):
    main_algorithm(denominator / numerator)

for i in range(len(numbers_list)):
    print("a" + str(i) + ": " + str(numbers_list[i]))
