number = int(input("Give a number: "))
str_number = str(number)
digits_sum = 0

for i in range(len(str_number)):
    digits_sum += int(str_number[i])

if number > 0 and number % digits_sum == 0:
    print("This number is \"dividable\"")
else:
    print("This number is not \"dividable\"")
