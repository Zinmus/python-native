max_number = int(input("Max number: "))
amicable_numbers_list = []

def divisors_sum(number):
    suma = 0
    for i in range(1, number):
        if number % i == 0:
            suma += i
    return suma

def has_pair(number):
    pair_number = divisors_sum(number)
    if divisors_sum(pair_number) == number and number < pair_number <= max_number:
        return True

def find_amicable_numbers(min_number, max_number):
    for i in range(min_number, max_number):
        if has_pair(i):
            amicable_numbers_list.append([i, divisors_sum(i)])

find_amicable_numbers(1, max_number)

print(amicable_numbers_list)
