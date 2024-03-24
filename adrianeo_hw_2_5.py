"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 01-26-2024
Homework Problem # 2_5
This program will iterate over numbers from 1 to 30 and print "foo", "bar", "baz", or their combinations based on these division rules:
•	If the number is divisible by 2, print the word foo
• If the number is divisible by 3, print the word bar
•	If the number is divisible by 5, print the word baz
•	If the number is divisible by more than one of these, print the combination on the same line.
•	If the number is not divisible by 2,3 or 5, do not print a string.
•	Print the output of each number in the loop on a single line as n: <string> 
After completing the sequence with a for loop, do the same with a while loop.
"""

"""Fizz-Buzz Challenge Program"""

# Part a: Declare a constant variable MAXVAL
MAXVAL = 30

# Part b & c: For loop from 1 to MAXVAL
for e in range(1, MAXVAL + 1):
    output = ""
    if e % 2 == 0:
        output += "foo"
    if e % 3 == 0:
        output += "bar"
    if e % 5 == 0:
        output += "baz"
    print(f"{e}: {output}")

# Part d: Print a separator line
print("-" * 20)

# Part e: While loop from 1 to MAXVAL
e = 1
while e <= MAXVAL:
    output = ""
    if e % 2 == 0:
        output += "foo"
    if e % 3 == 0:
        output += "bar"
    if e % 5 == 0:
        output += "baz"
    print(f"{e}: {output}")
    e += 1
