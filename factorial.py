
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)


n=int(input("Enter The positive number for Factorial : "))
if n<0:
    print("Factorial is not defined on negative number")
else:
    print(factorial(n))
    