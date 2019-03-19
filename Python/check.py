ch = input("Enter any thing: ")


if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        print("Is alphabet ", ch)
    
elif(ch >= '0' and ch <= '9'):
        print("Is a digit ",  ch)
    
else:
        print(" Is a whitespace character ", ch)
    
