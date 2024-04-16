def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        final_price=price + (price*(discount_percent * 0.01))
        print("Your final price is:") 
        return final_price
    else:
        final_price=price
        print("Your final price is:") 
        return final_price

#getting inputs
p=(int(input("Enter price: \n")))
d=(int(input("Enter the discount without the percent sign(%):\n")))
print(f"Your price is {p} and your discount percentage is {d}%\n")

#calling the function
print(calculate_discount(p,d))