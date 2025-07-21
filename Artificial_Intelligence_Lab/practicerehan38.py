def is_armstrong(number):
    # Convert number to string to iterate digits
    digits = str(number)
    power = len(digits)
    
    # Calculate the sum of digits raised to the power
    total = sum(int(digit) ** power for digit in digits)
    
    # Check if sum equals the original number
    return total == number

# Example usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

