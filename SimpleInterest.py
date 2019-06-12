def simpleInterest(principle, rate, time):
    si = (principle * rate * time) / 100
    return si
principle = eval(input("Enter principle(amount) : "))
rate = eval(input("Enter rate of interest : "))
time = eval(input("Enter unit of time : "))
simple_interest = simpleInterest(principle, rate, time)
print("Simple Interest : ", simple_interest)