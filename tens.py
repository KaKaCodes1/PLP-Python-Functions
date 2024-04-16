#Checks whether or not a number is divisible by ten.

def divisible_by_ten(num):
    if num%10==0:
        return True
    else:
        return False
    
#getting an input
z=(int(input("Enter a number for testing:\n")))

#calling the function
print(divisible_by_ten(z))