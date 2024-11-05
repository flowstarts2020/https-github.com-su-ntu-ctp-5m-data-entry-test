def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return "Error: Input must be a string."

    reversed_string = s[::-1]
    
    return reversed_string
# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
result1 = string_reverse("Hello World")
print("Reversed string for 'Hello World':", result1)

result2 = string_reverse("Python")
print("Reversed string for 'Python':", result2)
