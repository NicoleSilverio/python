from random import randint
import math
lists=[]
randomtimes=[]
for i in range (100):
    randomtimes.append(randint(10,99))

def numbers(randomtimes):
    for every_number in randomtimes:
        for every_number2 in randomtimes:
            if every_number2+every_number==99:
                lists.append(every_number)
                lists.append(every_number2)
    print(lists)
numbers(randomtimes)

#print(randomtimes)
