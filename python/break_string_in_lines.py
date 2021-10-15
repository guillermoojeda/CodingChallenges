# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or
# less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount
# of words. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each
# word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
# ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

def append_word(line, word):
    if line == "":
        return word
    else:
        return line + " " + word


def my_sep(s, k):
    my_list = s.split()
    current_line = ""
    answer = []
    count = 0
    for i in my_list:
        if len(append_word(current_line, i)) <= k :
            current_line = append_word(current_line, i)
        else:
            answer.append(current_line)
            current_line = i
            if count == len(my_list) - 1:
                answer.append(current_line)
        count += 1
    return answer


my_string = "the quick brown fox jumps over the lazy dog"
k = 10

print (my_sep(my_string, k))