# ASSIGNMENT DETAILS
# Name: Sonya Bourgeois
# Course: CSC500-1
# Module: 1:  Critical Thinking Part 2

# Define the multiplication function:
def multiplication(num1, num2):
    return num1 * num2

# Define the division function:
def division(num1, num2):
    return num1/num2

# Define Main Function
def main():
    # Obtain two numbers from user:
    num1 = float(input("First number, please:"))
    num2 = float(input("And now the second:"))
    
    # Perform multiplication and division functions using input from user:
    product_result = multiplication(num1, num2)
    quotient_result = division(num1, num2)
    
    # Print the resulting calculations:
    print("Multiplication:", product_result)
    print("Division:", quotient_result)

# Call the main function
if __name__ == "__main__":
    main()