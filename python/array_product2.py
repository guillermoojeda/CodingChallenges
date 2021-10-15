# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
# [3, 2, 1], the expected output would be [2, 3, 6].


def my_fun(some_arr):

    my_ans = []

    for i in some_arr:
        my_arr = some_arr  # remove this line to see that not behaving as expected.
        my_arr2 = my_arr
        my_arr2.remove(i)
        ans = 1
        for j in my_arr2:
            ans *= j
        my_ans.append(ans)
    return my_ans

print(my_fun([1, 2, 3, 4, 5]))