# count the number of vowels
def count_letter(phrase,letter):
    return list(phrase).count(letter)

def count_vowels(phrase):
    vowels = ['a','e', 'i', 'o', 'u']
    count = 0
    count_words = {}
    for rec in phrase:
        if rec in count_words:
            count_words[rec] += 1
        else:
            count_words[rec] = 1
        if rec in vowels:
            count += 1

    return (count, count_words)



if __name__ == "__main__":
    phrase = "Welcome to the world of innovation , we are here for a change"
    print(count_vowels(phrase))

    print( count_letter(phrase, ' '))
