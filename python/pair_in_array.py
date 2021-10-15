# Given an array/list of numbers as input., and given a number X, write a function that tells me all possible pairs of
# numbers within that array that sum X. X is also an argument of thios function
# E.G.: myArr = [3, 4, 5, 6, 6, 8, 9] and X = 12, then my function (myArr, X) should return [3, 9], [4, 8], [6, 6]

my_input = [1, 2, 6, 6, 7, 8, 8, 12, 4, 4]
my_X = 16


def my_fun(my_arr, x):
    pairs = []
    counter = 1
    for i in my_arr:
        other_arr = my_arr[counter:]
        for j in other_arr:
            if i + j == x:
                pairs.append([i, j])
        counter += 1
    return pairs


print(my_fun(my_input, my_X))
