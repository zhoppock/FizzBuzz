"""
Create a program the runs the numbers 1 through 100 with the following conditions:
 1. If a number is a multiple of 3, the program prints "Fizz" instead of that number.
 2. If a number is a multiple of 5, the program prints "Buzz" instead of that number.
 3. If a number is a multiple of both 3 and 5, the program prints "FizzBuzz" instead of that number.
"""
def FizzBuzz(start, end):
    for num in range(start, end):
        print(("Fizz" * (num % 3 == 0)) + ("Buzz" * (num % 5 == 0)) or str(num), end = " ")

def main():
    start = 1
    end = 101
    FizzBuzz(start, end)

main()