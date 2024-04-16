#Checking whether the result of taking the power of one number to another number provides an answer which is greater than 5000.
def large_power(base,exponent):
    result=base**exponent
    if result > 5000:
        return True
    else:
        return False

#getting the inputs   
x=(int(input("Enter the base value:\n")))
y=(int(input("Enter the exponent value:\n")))

#calling the function
print(large_power(x,y))