"""
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
"""
num = int (input("enter an integer: "))
if num%2 == 0:
    print("the number is even")
else:
    print("the number is odd")