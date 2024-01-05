## Counting the number of letters, numbers, and speccial Characters in a phrase

import re

name = "Esaakki are you belong to 2023 Batch :) am i wrong here ???"

spChar = "!@#$%^&*()"

digi_count = re.sub("[^0-9]", "",name)
letter_count = re.sub("[^a-zA-Z]", "",name)
space_count = re.findall("[ \n]", name)
special_ch_count = re.sub("[\w]+","",name)

print(len(digi_count))
print(len(letter_count))
print(len(space_count))

print(len(special_ch_count))

print("__" * 30)

a=[[]]*5
a[0].append(1)
print(a)