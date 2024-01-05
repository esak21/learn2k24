#Write a program that accepts input in this form: s3t1z5.
# Here any character is followed by a number.
# The program should return a string where the character is repeated for the corresponding number of times.


def convert_to_letters(digi_chars):
    res = ""
    for i in range(0, len(digi_chars), 2):
        # taking 2 chars at a time

        for j in range(int(digi_chars[i+1])):

            res = res + digi_chars[i]

    print(res)



if __name__ == "__main__":
    digi_chars = "a3e2s4z4"
    convert_to_letters(digi_chars)