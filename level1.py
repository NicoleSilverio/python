from random import randint



randomtimes=[]
for i in range (100):
    randomtimes.append(randint(10,99))
print(randomtimes)


def onlist(random):
    for item in random:
        if (item % 5)== 0:
            print(item)
onlist(randomtimes)
