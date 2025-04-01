def calculate_discount(price,discount_percent):
    #the function checks if the percentage is greater or equal to 20%
    if discount_percent >= 20:
     discount_amount= price * (discount_percent/100)
     result = price-discount_amount 
     return f"The priceis now {result}"
    else:
        return f"The price is {price}" 

print(calculate_discount(price= float(input("Enter the original price: ")),discount_percent= float(input("Enter a percentage: "))))