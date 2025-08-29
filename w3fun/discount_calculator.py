def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item in Birr: "))
    discount_input = input("Enter the discount percentage: ")
    
    # Remove any percentage symbols and convert to float
    discount_input = discount_input.replace('%', '').strip()
    discount_percentage = float(discount_input)
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display results
    if discount_percentage >= 20:
        print(f"Original price: {original_price:.2f} Birr")
        print(f"Discount applied: {discount_percentage}%")
        print(f"Final price after discount: {final_price:.2f} Birr")
    else:
        print(f"No discount applied (discount was only {discount_percentage}%)")
        print(f"Final price: {final_price:.2f} Birr")
        
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")