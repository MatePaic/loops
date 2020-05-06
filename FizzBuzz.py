number = int(input('Select a number between 1 and 100: '))
for i in range(1, number + 1):
    if number > 100:
        print('Must be smaller than 100')
        break
    elif i % 5 == 0 and i % 3 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
