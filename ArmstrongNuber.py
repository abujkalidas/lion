def order(number):
    n = 0
    while number != 0:
        number = number // 10
        n = n + 1
    return n

def isArmstrong(number):
    n = order(number)
    temp = number
    sum = 0
    while temp != 0:
        rem = temp % 10
        sum += pow(rem, n)
        temp //= 10
    return (number == sum)

number = int(input("Enter a number : "))
armstrong = isArmstrong(number)
if armstrong:
    print(number, "ia a armstrong number...!!!")
else:
    print(number, "ia a not armstrong number...!!!")


