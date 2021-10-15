# Given an array of seros and ones, where a series of 1s are parts of rivers,
# and the number of adjacent (not diagonal) 1s determine a river´s size, write a function that returns an array
# of the sizes of all rivers in the input matrix. Sizes do not need to be in a particular order.

# exec(open("filename.py").read())
# exec(open("C:/pythonProjects/code_training/river_sizes.py").read())


my_input = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

# The corresponding output should be:

my_output = [1, 2, 2, 2, 5]


# Code starts here


def get_neighbours(matrix, coordX, coordY):
    # my_input is the matrix, coord is entered as [X, Y], e.g.: [2, 5]
    # Returns neighbors as an array of zeros and ones, where corresponding positions are [N, E, S, W]

    answer = [0, 0, 0, 0]

    # North Neighbor
    if coordX > 0:
        answer[0] = matrix[coordX - 1][coordY]

    # East Neighbor
    if coordY < len(matrix[coordX]) - 1:
        answer[1] = matrix[coordX][coordY + 1]

    # South Neighbor
    if coordX < len(matrix[1]) - 1:
        answer[2] = matrix[coordX + 1][coordY]

    # West Neighbor
    if coordY > 0:
        answer[3] = matrix[coordX][coordY - 1]

    return answer


def myfun(matrix):
    lengths_list = []
    checked_list = []
    counti = 0
    for i in matrix:
        countj = 0
        for j in i:
            print(" ")
            print("counti is", counti)
            print("countj is", countj)
            if matrix[counti][countj] == 1 and [i, j] not in checked_list:
                print("We found a one")
                if (get_neighbours(matrix, counti, countj).count(1) == 1 or
                    get_neighbours(matrix, counti, countj).count(1) == 0) and \
                        ([counti, countj] not in checked_list):  # If evaluates true, this spot is
                    # the extreme of a river so that has not been checked, we start counting tiles with "1".

                    print("It is an extreme!")

                    counter = 0
                    marker = [counti, countj]
                    checked_list.append([marker[0], marker[1]])
                    first_river_tile = True  # Because we are evaluating the first river tile.

                    # Start evaluating from second tile of water onwards.

                    while get_neighbours(matrix, marker[0], marker[1]).count(1) > 0 or first_river_tile:

                        print("We keep counting")

                        flow_direction = [0, 0]

                        print("Marker is at", marker)
                        print("Ckecked list is", checked_list)

                        neighbours = get_neighbours(matrix, marker[0], marker[1])
                        if 1 in neighbours:
                            print("This water tile has neighboring water")
                            print (neighbours)
                        if neighbours[0] == 1 and [marker[0]-1, marker[1]] not in checked_list:
                            flow_direction = [-1, 0]
                        if neighbours[1] == 1 and [marker[0], marker[1]+1] not in checked_list:
                            flow_direction = [0, +1]
                        if neighbours[2] == 1 and [marker[0]+1, marker[1]] not in checked_list:
                            flow_direction = [+1, 0]
                        if neighbours[3] == 1 and [marker[0], marker[1]-1] not in checked_list:
                            flow_direction = [0, -1]

                            print("Flow direction is", flow_direction)

                        if flow_direction != [0, 0]:
                            marker[0] += flow_direction[0]
                            marker[1] += flow_direction[1]
                            if 0 <= marker[0] <= 5 and 0 <= marker[1] <= 5 and matrix[marker[0]][marker[1]] == 1:
                                checked_list.append([marker[0], marker[1]])
                        counter += 1
                        print(" ")

                        first_river_tile = False

                        if flow_direction == [0, 0]:
                            print("No more water that is not checked for this river")
                            print(" ")
                            break

                    river_length = counter
                    lengths_list.append(river_length)
                    print("Length of", counter, "appended to list.")

            countj += 1
        counti += 1

    lengths_list.sort()
    return lengths_list


# Testing


print(myfun(my_input))

print(get_neighbours(my_input, 0, 0))
