def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n=int(input("Enter a non negative number"))
if n<0:
    print("enter a valid non negative number")
else:
    print('Fiboancci number at position',n,'is',fibonacci(n))