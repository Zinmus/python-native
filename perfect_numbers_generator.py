max_number = int(input("Max number: "))
perfect_numbers_list = []

def is_perfect(number):
    suma = 0
    for i in range(1, number):
        if number % i == 0:
            suma += i
    if number == suma:
        return True

def find_perfect_numbers(min_number, max_number):
    for i in range(min_number, max_number):
        if is_perfect(i):
            perfect_numbers_list.append(i)

find_perfect_numbers(1, max_number)

print(perfect_numbers_list)        
        
