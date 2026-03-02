# Module 7 Assingment Using Loops in Python
# This program creates a list of 15 numbers
# It determines whether each number is odd or even

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for number in numbers:
    if number % 2 == 0:
        print(str(number) + "is even")
    else:
        print(str(number) + "is odd")
