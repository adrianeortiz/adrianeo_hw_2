"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 01-26-2024
Homework Problem # 2_4
This program uses the modulus operator % to determine if the input number is odd or even. If a number is divisible by 2 (even), the modulus operation n % 2 will result in 0. If it's not divisible by 2 (odd), the result will be 1.
"""

# Prompt for a number
user_number = input("Enter a number: ")

# Convert the input to an integer
num_to_int = int(user_number)

# Print 0 if even, 1 if odd
print(num_to_int % 2)
