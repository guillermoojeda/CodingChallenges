# Binary tree
# Given a number, tell what row is it located in a binaty tree.
# A binary tree is like:
#     1
#    2 3
# 4 5   6 7

# And so on. 2 is in row "1", 7 is in row "2"

def my_fun(number):
    current_row = 0
    max_num = 1
    current_positions = 1
    if number == 1:
        return current_row
    while number > max_num:
        current_positions *= 2
        max_num = max_num + current_positions
        current_row += 1
        if number <= max_num:
            return current_row

print (my_fun(100))
        
    
