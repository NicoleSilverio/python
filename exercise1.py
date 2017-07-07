import math
def radius():
    radius = int(input("what radius do you want?"))


def volume(radius):
    v = (4/3) * math.pi * radius**3
    return v
print(volume(radius))
#everything worked up until this code.
def area(radius):
    A = 4 * math.pi * radius**2
    return A
print(area(radius))


print("volume or area?")
answer1= input("volume or area?")
if answer1=="volume":
    radius()
    volume()
else:
    if answer1=="area":
        radius()
        area()
