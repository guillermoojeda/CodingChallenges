# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct
# characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def my_fun(some_string, k):
    counter1 = 0
    longest = ""
    for i in some_string:
        counter2 = counter1
        for j in some_string[counter1:]:
            string_eval = some_string[counter1:counter2+1]
            print (string_eval)
            if len(string_eval) > len(longest) and len(set(string_eval)) <= k:
                longest  = string_eval
            counter2 += 1
        counter1 += 1
    return len(longest)


print(my_fun("abcba", 2))
