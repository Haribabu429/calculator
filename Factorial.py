import math

f = int(input("Enter the factorial number: "))
if f == 1:
    print("Factorial of 1 is 1")
elif f == 2:
    print("The factorial of 2 is 2")
else:
    fact = 1
    for i in range(2, f+1):
        fact *= i
    print("The factorial value of {} is {}".format(f, fact))

K = int(input("Enter the factorial number: "))
print(math.factorial(K))


# The above code is factorial code. 
# next comment
