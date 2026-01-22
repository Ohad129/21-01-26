print('there are 10 movies you need to rate, rate each one by order')
i: int = 0
low: int = 5
high: int = 1
while i < 10:
    print('movie number:' , i + 1)
    rating = int(input('your rating? '))
    if 1 <= rating <= 5:
        i += 1
        if low > rating:
            low = rating
        if high < rating:
            high = rating
    else:
        print('invalid input')
print('the highest grade is:' , high)
print('the lowest grade is:' , low)