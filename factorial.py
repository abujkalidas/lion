def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)

number = int(input("Enter a number :"))
print("Factorial of ", number, "is", fact(number))
