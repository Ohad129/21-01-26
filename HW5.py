i: int = 0
amount: int = 0
num = int(input('enter number of students: '))
while i < num:
    print('student number:' , (i + 1))
    grade = int(input('His grade is: '))
    if 0 <= grade <= 100:
       amount += grade
       i += 1
    else:
        print('Enter valid grade!')
print('The average grade is:' , amount // num)