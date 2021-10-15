# Given an array of unrepeated numbers (or characters, or whatever), find all possible subsets of that sets. Remember
# that an empty set is a subset of it, and a set that is the same as it is also a subset of it.
# E.G.: For {1, 2}, the function should print {}, {1}, {2}, {1, 2}

my_array = [1, 2, 3, 4]


def print_set(subset):
    subset_copy = []
    for i in subset:
        if i != "v":
            subset_copy.append(i)
    print(subset_copy)


def helper(given_array, subset, i):
    if i == len(given_array):
        print_set(subset)
    else:
        subset[i] = "v"
        helper(given_array, subset, i + 1)
        subset[i] = given_array[i]
        helper(given_array, subset, i + 1)


def all_subsets(given_array):
    subset = ["v"] * len(given_array)  # "v" for "void", or Null if preferred. A trick so I do not need to shorten the
    #  array with different iterations. Instead, I will remove "v" before printing it.
    helper(given_array, subset, 0)


all_subsets(my_array)