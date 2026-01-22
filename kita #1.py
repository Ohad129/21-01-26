'''
# 1
num: int =int(input("Enter number of classes:"))
cnt: int = 1
while cnt <= num:
    print(cnt)
    cnt += 1

# 2
student: int =int(input("Enter number of students:"))
avg: int = 0
i: int = 0
while i < student:
    grade: int = int(input("enter grade:"))
    avg += grade
    i += 1
print("The average is: " , avg // student)
'''
#3
x: int = 1
while x <= 10:
    y: int = 1
    while y <= 10:
        print(x * y)
        y += 1
    x += 1


