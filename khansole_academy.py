"""
Now that you've seen how programming can help us in a number of different areas,
it's time for you to implement Khansole Academy—a program that helps other people
learn! In this problem, you'll write a program in the file khansole_academy.py
that randomly generates addition problems for the user, reads in the answer from
the user, and then checks to see if they got it right or wrong, until the user
appears to have mastered the material.

More specifically, your program should be able to generate addition problems that
involve adding two 2-digit integers (10 through 99, inclusive). The user should be
asked for an answer to each problem. Your program should determine if the answer
was correct or not, and give the user an appropriate message to let them know.

Your program should keep giving the user problems until the user has gotten 3
problems correct in a row. (Note: the number of problems the user needs to get
correctly in a row to complete the program is just one example of a good place
to specify a constant in your program).

Once this is done, expand the game to include subtraction, multiplication, and division.
"""

import random


def main():
    """
    Have the user answer 3 addition or multiplication questions in a row.
    """
    print("Welcome to Khansole academy! Get three questions correct in a row to beat the game.")

    print("Congrats! You did it!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
