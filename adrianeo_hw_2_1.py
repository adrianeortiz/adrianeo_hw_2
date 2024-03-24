"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 01-26-2024
Homework Problem # 2_1
I have to write a Python program that does the following:
Prompts the user to enter a whole number from 1 to 7. Then performs these operations on it in this order: Multiply by 2, Add 10, Divide by 2, Subtract the user supplied number. Then print the output of this calculation as an integer. Then take the same number and convert it to a three‐digit number with incrementing digits and assign this number to a variable of type int. Afterwards, add the three digits together and print the results. Then divide the three‐digit version by the sum of the digits and print the results as a float. Lastly, reprint the division as a truncated integer.
"""

# Part a: Prompt user to enter a number between 1 and 7
user_input = int(input("Enter a whole number from 1 to 7: "))

# Part b: Perform operations and Part c: print the result as an int
result_b = ((user_input * 2 + 10) / 2) - user_input
print("The integer result after the calculations is: ", int(result_b))

# Part d: Convert to a three-digit number with incrementing digits
three_digit_number = int(f"{user_input}{user_input + 1}{user_input + 2}")
print("The 3 digit version of your number is: ", three_digit_number)

# Part e: Add the three digits together and print result
sum_of_digits = user_input + (user_input + 1) + (user_input + 2)
print("The sum of your 3 digit number is: ", sum_of_digits)

# Part f: Divide the three-digit number by the sum of its digits and print result
division_result = three_digit_number / sum_of_digits
print("The result of the division as a float is: ", division_result)

# Part g: Reprint the output of part f as a truncated integer
print("The result of the division as an int is: ", int(division_result))


