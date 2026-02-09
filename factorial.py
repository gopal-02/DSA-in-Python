# # Program to find the factorial of a number
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result
# # Get user input
# number = int(input("Enter a number to find its factorial: "))
# # Calculate and print the factorial
# print(f"The factorial of {number} is: {factorial(number)}")


# factorial of a number using recursion
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
# Get user input
number = int(input("Enter a number to find its factorial using recursion: "))
# Calculate and print the factorial
print(f"The factorial of {number} is: {factorial_recursive(number)}")