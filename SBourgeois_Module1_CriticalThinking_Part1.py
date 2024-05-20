# ASSIGNMENT DETAILS
# Name: Sonya Bourgeois
# Course: CSC500-1
# Module: 1:  Critical Thinking Part 1

# Define the addition function:
def addition(num1, num2):
    return num1 + num2

# Define the subtraction function:
def subtraction(num1, num2):
    return num1 - num2

# Define Main Function
def main():
    # Obtain two numbers from user:
    num1 = float(input("First number, please:"))
    num2 = float(input("And now the second:"))
    
    # Perform addition and subtraction functions using input from user:
    sum_result = addition(num1, num2)
    difference_result = subtraction(num1, num2)
    
    # Print the resulting calculations:
    print("Addition:", sum_result)
    print("Subtraction:", difference_result)

# Call the main function
if __name__ == "__main__":
    main()