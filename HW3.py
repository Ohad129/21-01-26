i: int = 0
amount: int = 0
num = int(input('enter number: '))
while num != -999:
    i += 1
    amount += num
    num = int(input('enter number: '))
print(i , 'numbers received')
print('the sum of all numbers is:' , amount)