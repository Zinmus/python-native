country_list = ['France', 'UAE', 'Netherlands', 'Turkey', 'Switzerland', 'Ukraine', 'Poland']
capital_list = ['Paris', 'Abu Dhabi', 'Amsterdam', 'Ankara', 'Bern', 'Kyiv', 'Warsaw']

mistake_number = 0
i = 0

while mistake_number < 3 and i < len(country_list):
    print('Country: ', country_list[i])
    capital = input('Name the capital of this country: ')
    if capital == capital_list[i]:
        print('Correct!')
    else:
        mistake_number += 1
        print('Wrong!')
    i = i + 1

if mistake_number == 0:
    print('Congratulations! You are an expert in geography!')
elif mistake_number == 1:
    print('Not bad! You can go on a trip!')
elif mistake_number == 2:
    print('You should study geography a little bit more!')
else:
    print('You should stay at home!')
