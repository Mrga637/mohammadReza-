list1 = []
number = 0
sum = 0
while number >= 0:
    number = int(input('add begoo'))
    if number>=0 :
        list1.append(number)
a = int(len(list1))
while a > 0 :
    print(list1[a-1])
    sum = sum +list1[a-1]
    a-=1
sum = sum / len(list1)
print(sum)
print(list1)
