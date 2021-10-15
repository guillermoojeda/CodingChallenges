# First function: Given a string, take that string and return the first recurring character on that string.
# Second function: Given a string, take that string and return the first nono-recurring character on that string.

input_string = "abcdefghijdklmenoabcdef"


def my_fun(string):
    my_list = []
    for i in string:
        if i in my_list:
            return i
        else:
            my_list.append(i)
    return("No recurring character found")

def my_fun2(string):
    my_list = [] # List of already existant chars
    my_list2 = []  # List of recurring existant chars
    for i in string:
        if i in my_list:
            my_list2.append(i)
        else:
            my_list.append(i)
    for i in string:
        if i not in my_list2:
            return i

    return("No non-recurring character found")

print(my_fun(input_string))
print(my_fun2(input_string))
