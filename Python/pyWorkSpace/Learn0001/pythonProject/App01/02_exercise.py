# Find Factorial of a number

def factorial_of_number(number):
    if number == 0:
        return 1
    else:
        return number * factorial_of_number( number-1 )


if __name__ == "__main__":
    result = factorial_of_number(5)
    print(result)