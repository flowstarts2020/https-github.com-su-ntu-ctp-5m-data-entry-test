def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return "Error: Both num and divisor must be numeric."
    
    if divisor == 0:
        return "Error: Division by zero is not allowed."
    return

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
result1 = check_divisibility(10, 2)
print("Result for (10, 2):", result1)

result2 = check_divisibility(7, 3)
print("Result for (7, 3):", result2)
