"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 01-26-2024
Homework Problem # 2_3
When you run this program, it will prompt the user to enter a number, then calculate (n^3 / n), and print the result formatted to two decimal places.	
"""

def calculate_and_print():
    # Part a: Prompt the user to enter a number
    user_number = float(input("Please enter a number: " ))

    # Part b: Compute user_number cubed divided by user_number
    result = (user_number ** 3) / user_number

    # Part c: Print the formula and results
    print(f"{user_number} ** 3 / {user_number} = {result:.2f}")

# Execute the function
calculate_and_print()




