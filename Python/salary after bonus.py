sal = input("Enter Your Salary: ")
gen = eval(input("Enter your Gender(M\F): "))


if(gen=="M" or gen=="m"):
        if(sal<10000):
            print("Salary after Bonus: ",bonus=0.7*sal)
        else:
            print("Salary after Bonus: ",bonus=0.5*sal)

elif(gen=="F" or gen=="f"):
        if(sal<10000):
              print("Salary after Bonus: ",bonus=0.9*sal)

        else:
              print("Salary after Bonus: ",bonus=0.7*sal)
