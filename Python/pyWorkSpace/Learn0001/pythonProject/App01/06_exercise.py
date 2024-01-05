# find the second largest number in the list

def find_largest_number(numbers):
    first_largets_number = max(numbers)
    print(f"First largest Number {first_largets_number}")
    largest_number = 0
    second_largest = 0

    for num in numbers:
        if num > largest_number:
            second_largest = largest_number
            largest_number = num
        elif num > second_largest and num != largest_number:
            second_largest = num

    return second_largest




if __name__ == "__main__":
    print( find_largest_number([10,20,23,33,441,234]))
