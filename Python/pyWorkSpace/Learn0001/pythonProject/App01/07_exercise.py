# REmove duplicates from the List

def remove_duplicates2(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers


def remove_duplicates(numbers):
    new_numbers = set(numbers)
    return list(new_numbers)

if __name__ == "__main__":
    print( remove_duplicates2([10,10,23,45,45,54,54]) )
