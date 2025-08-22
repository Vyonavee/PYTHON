def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item
    discount_percent (float): The discount percentage to apply
    
    Returns:
    float: The final price after discount (if applicable)
    """
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate final price after applying discount
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return original price
        return price

# Get input from the user
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using our function
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display the results
    print(f"\nOriginal price: ${original_price:.2f}")
    print(f"Discount percentage: {discount_percentage}%")
    
    if discount_percentage >= 20:
        print(f"Final price after discount: ${final_price:.2f}")
        print(f"You saved: ${original_price - final_price:.2f}")
    else:
        print(f"No discount applied (discount must be 20% or higher)")
        print(f"Final price: ${final_price:.2f}")
        
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")