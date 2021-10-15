# Good morning! Here's your coding interview problem for today.
#
# This question was asked by Zillow.
#
# You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0],
# and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.
#
# For example, in this matrix
#
# 0 3 1 1 5
# 2 0 0 4 7
# 1 5 3 1 8
#
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 25 coins.

all_values = []

my_matrix = [[0, 3, 1, 1, 5], [2, 0, 0, 4, 7], [1, 5, 3, 1, 8]]


def sum_and_move(current_value, r, c, matrix):
    if r < len(matrix) and c < len(matrix[0]):
        current_value += matrix[r][c]
        all_values.append(current_value)
    if r == len(matrix) and c == len(matrix[0]):
        print("Branch ended")
    if c <= len(matrix[0]):
        sum_and_move(current_value, r, c+1, matrix)
    if r <= len(matrix):
        sum_and_move(current_value, r+1, c, matrix)


if __name__ == "__main__":
    sum_and_move(my_matrix[0][0], 0, 0, my_matrix)
    print("Answer is: " + str(max(all_values)))
    print(all_values)

