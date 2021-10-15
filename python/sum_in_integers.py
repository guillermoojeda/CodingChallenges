# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
# since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

my_string = [2, 4, 6, 2, 5]

def my_fun(input_string):
    largest_index = [0]
    largest_number = 0
    largest_index2 = [0]
    largest_number2 = 0
    largest_index3 = [0]
    largest_number3 = 0
    largest_index4 = [0]
    largest_number4 = 0
    counter = 0
    for i in input_string:
        if i > largest_number:
            largest_number2 = largest_number
            largest_number = i
            largest_index2 = largest_index
            largest_index = counter
        elif i > largest_number2:
            largest_number2 = i
            largest_index2 = counter
        counter += 1
    return(largest_number + largest_number2)

print (my_fun(my_string))