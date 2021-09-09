number = int(input('add begoo '))
numbers = []
while number>= 0 :
    number = int(input('add begoo '))
    numbers.append(number)
    if number < 0 :
        print(numbers)
        x = len(numbers)
        i = numbers / x
        print(i)
