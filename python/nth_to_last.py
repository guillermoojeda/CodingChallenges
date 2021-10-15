# Given a singly linked list, write a function to find the nth-to.last element of the list
# E.g.: list = [1, 2, 3, 4, 5], always increases one by one, and starts at one
# my_fun(list, 3) should return 2

my_list = list = [1, 2, 3, 4, 5]


def my_fun(some_list, n):
    lenght = len(some_list)
    ans = lenght - n
    return ans


print(my_fun(my_list, 2))
