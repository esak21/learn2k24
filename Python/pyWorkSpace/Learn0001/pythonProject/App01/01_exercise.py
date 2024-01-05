# check if the String is Palindrome or not


# we need to reverse the string and compare it

def is_palindrome( original_string):
    another_string = original_string[::-1]
    print(another_string)

    if another_string == original_string:
        print(f"Given String {original_string} is Palindrome")
    else:
        print(f"Given String is not palindrome")



if __name__ == "__main__":
    is_palindrome("madam")