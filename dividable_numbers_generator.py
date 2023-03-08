def is_dividable(number):
    str_number = str(number)
    digits_sum = 0

    for i in range(len(str_number)):
        digits_sum += int(str_number[i])

    if number > 0 and number % digits_sum == 0:
        return True
    else:
        return False

for i in range(1,10000):
    if is_dividable(i):
        print(i)
