# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string which we can delete at most k, return whether you can make a palindrome.
#
# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

palindrome_list = []


def is_palindrome(string):
    if string == string[::-1]:
        print(string + " is a palindrome.")
        return True
    else:
        return False


def recursion_search(string, k):
    print("")
    print("k is " + str(k))
    print("String is " + string)
    if is_palindrome(string):
        print(string + " is a palindrome.")
        palindrome_list.append(string)
    if k == 0:
        print("End of branch.")
        print("")
    else:
        s1 = string
        for i in range(0, len(s1)):
            s2 = s1[:i] + s1[i + 1:]
            print("s1  is " + s1)
            print("s2  is " + s2)
            recursion_search(s2, k - 1)


if __name__ == '__main__':
    myString = "waterrfetawx"
    print("Starting code")
    recursion_search(myString, 3)
    print(palindrome_list)
