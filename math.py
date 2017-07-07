def fibseries(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibseries(n-1) + (n-2)

x = input("number?")

print(fibseries(int(x)))
