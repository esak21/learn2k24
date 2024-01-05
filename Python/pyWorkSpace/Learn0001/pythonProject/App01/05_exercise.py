# FInd Common elements between 2 lists
import sys


def compare_two_list_easy(first, second):
    common = []
    for item in first:
        if item in second:
            common.append(item)
    return common


def compare_two_lists(first, second):
    common_elements = []
    if len(first) != len(second):
        sys.exit()
    else:
        for i in range(0, len(first)):
            print(i)
            temp = first[i]
            for j in range(0, len(second)):
                if second[j] == temp:
                    common_elements.append(second[j])
            else:
                print("Words didnt Match")
                continue

    return common_elements

def count_occurance(numbers:list, ele):
    return numbers.count(ele)

def total_occurance(numbers:list):
    count = {}
    for rec in numbers:
        if rec in count:
            count[rec] +=1
        else:
            count[rec] = 1
    return count

if __name__ == "__main__":
    first = ["esakki", "are", "you", "ready"]
    second = ["Esakki", "you", "are", "useful"]

    print(compare_two_lists(first, second))
    numbers = ["esakki","esakki","is", "a","hero", "or","a","villan"]

    print(count_occurance(numbers, 'a'))

    print(total_occurance(numbers))




