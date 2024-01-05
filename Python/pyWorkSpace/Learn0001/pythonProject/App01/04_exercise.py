# find the frequency of each element in a list

def count_frequency(words):
    count_words = {}
    for rec in words:
        if rec in count_words:
            count_words[rec] += 1
        else:
            count_words[rec] = 1

    return count_words


if __name__ == "__main__":
    words = ["apple", "orange", '', "orange","cow", "cow"]
    print( count_frequency(words))
