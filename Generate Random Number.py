print("To Generate Random Prime Number ")

#for prime_number in an interval set the loer and upper limit

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))


for num in range(lower,upper+1):
    if num > 1:
        for i in range (2,num):
            if (num%i)==0:
                break

        else:
            print(num)
