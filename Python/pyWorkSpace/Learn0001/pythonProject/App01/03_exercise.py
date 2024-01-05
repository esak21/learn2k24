# Find the Largest Number in a List


def find_largest_number(numbers):
    max_value = 0
    for number in numbers:
        if number > max_value:
            max_value = number
        else:
            continue
    return max_value


if __name__ == "__main__":
    marks = [89,56,2,12,78,178,102]
    print(find_largest_number(marks))