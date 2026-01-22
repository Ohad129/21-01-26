number = int(input('enter number: '))
if number % 2 == 0:
    print('2')
if number % 3 == 0:
    print('3')
if number % 5 == 0:
    print('5')
if number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
    print('no small dividers')