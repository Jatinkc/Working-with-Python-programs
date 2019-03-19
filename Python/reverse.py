num=int(input("Enter a 3 digit number:" ))
rem = num % 10
num = num // 10
rem1=num%10
num=num//10
rem2=num%10
num=rem*100+rem1*10+rem2
print("Reverse of the number:", num)
