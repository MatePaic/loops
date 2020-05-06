print('Greetings! We are here to convert unit')

while True:
    kilometers = input('Enter number of kilometers: ')
    kilometers = float(kilometers.replace(',', '.'))
    miles = kilometers * 0.621371192
    print(f'Conversion from {kilometers} kilometers is {miles} miles: ')
    another_conversion = input('y/n: ')
    if another_conversion.lower() != 'y' and another_conversion.lower() != 'yes':
        break


