"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 01-26-2024
Homework Problem # 2_2
This program prompts the user for input, attempts to print it in three formats, and includes a docstring explaining which inputs won't cause errors.	
"""

def print_input_three_ways():
    """
    This function prompts the user to enter a string or a number, then prints the input three times: as a string, an integer, and a floating-point value. It also includes a docstring comment at the end explaining which data types can be input without generating any errors.
    """

    # Part a: Prompt user to enter a string or a number
    user_input = input("Enter a string or a number: ")

    # Part b: Print the input three ways
    try:
        # As a string
        print(f"String: {user_input}")

        # As an integer
        print(f"Integer: {int(user_input)}")

        # As a float
        print(f"Float: {float(user_input)}")
    except ValueError:
        print("Error: The input cannot be converted to an integer or float.")

    """
    The only data types that can be input without generating any errors are numeric strings that can be converted to both an integer and a float. This is because the program attempts to cast the user input to an integer and a float. If the input is a string that does not represent a number (like "hello"), then the conversion to int or float will fail, causing a ValueError. Numeric strings (like "14" or "1.23") can be successfully converted to both integers and floats, so they will not cause an error in the program.
    """

# Execute the function
print_input_three_ways()
