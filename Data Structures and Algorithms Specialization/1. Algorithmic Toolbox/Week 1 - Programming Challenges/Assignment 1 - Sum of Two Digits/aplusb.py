'''
In this very first programming challenge, your goal is to implement a program that reads two digits from the standard input and prints their sum to the standard output.  We start from this ridiculously simple problem to show you the pipeline of reading the problem statement, designing an algorithm, implementing it, testing and debugging your program, and submitting it to the grading system. The starter solutions pack contains solutions to this problem in various programming languages. Submit a solution under the "My submission" tab.
'''

import sys

def print_sum_of_two_numbers(a: int, b: int) -> None:
    print(a+b)

if __name__ == "__main__":
    # a,b = int(input("Enter first number: ")), int(input("Enter second number: "))
    # a,b = int(sys.argv[1]), int(sys.argv[2])
    # a, b = map(int, input().split())
    a, b = map(int, [*input()])
    
    print_sum_of_two_numbers(a, b)
