# Given a string containing digits from 2 to 9, return all possible letter combinations that a number could represent:
# {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
# E.G: my_fun("23") should return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


num_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

given_number = "2432"


def print_set(subset):
    subset_copy = []
    for i in subset:
        if i != "v":
            subset_copy.append(i)
    print(subset_copy)


def helper(given_array, subset, i):
    if i == len(given_array):
        print("Printing subset")
        print_set(subset)
    else:
        #print("i is", i)
        #print("subset[i] is", subset[i])
        #print("given_array[i] is", given_array[i])

        subset[i] = num_dict[int(given_array[i])][0]
        helper(given_array, subset, i + 1)
        subset[i] = num_dict[int(given_array[i])][1]
        helper(given_array, subset, i + 1)
        subset[i] = num_dict[int(given_array[i])][2]
        helper(given_array, subset, i + 1)


def my_fun(given_array):
    subset = ["v"] * len(given_array)  # "v" for "void", or Null if preferred. A trick so I do not need to shorten the
    #  array with different iterations. Instead, I will remove "v" before printing it.
    helper(given_array, subset, 0)


my_fun(given_number)


