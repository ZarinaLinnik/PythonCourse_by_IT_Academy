# 4. Write a program that takes a list of numbers as input
# returns the second largest number in the list.

# The first version
# Bubble sort. Big O: n * n == n^2
list_of_num = [1, 3, 6, 9, 10, 33, 2, 1, 11]
for i in range(len(list_of_num)):
    for j in range(1, len(list_of_num)):
        if list_of_num[j-1] > list_of_num[j]:
            list_of_num[j-1], list_of_num[j] = list_of_num[j], list_of_num[j-1]
print('The first version:', list_of_num[-2])


# The second version
# The same Big O: n * n == n^2
list_of_num = [1, 3, 6, 9, 10, 33, 2, 1, 11]
for i in range(len(list_of_num)-1):
    min_obj, index = '', ''
    for j in range(i, len(list_of_num)):
        if min_obj == '' or min_obj > list_of_num[j]:
            min_obj, index = list_of_num[j], j
    list_of_num[i], list_of_num[index] = min_obj, list_of_num[i]
print('The second version:', list_of_num[-2])


# The third version
list_of_num = [1, 3, 6, 9, 10, 33, 2, 1, 11]
print('The third version:', sorted(list_of_num)[-2])  # This is worse for memory. Big O: O(n * log(2)n)


# The forth version
list_of_num = [1, 3, 6, 9, 10, 33, 2, 1, 11]
list_of_num.sort(reverse=True)  # This is better for memory
print('The forth version:', list_of_num[1])
