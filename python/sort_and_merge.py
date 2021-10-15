# Given n arrays, contained in an array called my_input, return a list that contains all the elenments inside those
# arrays, sorted.

arr1 = [3, 6, 7]
arr2 = [12, 4, 17]
arr3 = [1, 7, 9]
my_input = [arr1, arr2, arr3]


def fun1(arrs):
    my_arr = []
    for i in arrs:
        for j in i:
            my_arr.append(j)

    my_arr.sort()
    return my_arr

print (fun1(my_input))