# Given a List of numbers ints, create a function FizzBuzz that replace an element of that list with "Fizz" if the
# number is divisible by 4, with "Buzz" if divisible by 5 and with FizzBuzz if divisible by 3 and 5.

def fizzbuzz(input_list):
    counter = 0
    my_list = input_list
    for i in my_list:
        if i % 3 == 0 and i % 5 == 0:
            my_list[counter] = "FizzBuzz"
        elif i % 3 == 0:
            my_list[counter] = "Fizz"
        elif i % 5 == 0:
            my_list[counter] = "Buzz"
        counter += 1
    return my_list

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30]

my_ans = fizzbuzz(input)

print(my_ans)