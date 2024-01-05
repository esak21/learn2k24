## Write a program to count pairs of elements of a list with a given sum

l = [2,4,6,7,8,9,1,2,8, 6, 10, 3, 5]
sum = 12
count = 0
for i in range(0, len(l)):

    for j in range(i+1, len(l)):

        if l[i] + l[j] == sum :
            print(l[i],l[j])
            count += 1

print(count)