"""
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have
been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""


def overlaps(pair1, pair2):
    # can be contained, or overlapping
    # overlapping
    if pair1[0] <= pair2[0] <= pair1[1] or pair1[0] <= pair2[1] <= pair1[1]:
        # then, they overlap
        if pair1[0] <= pair2[0]:
            new_bottom = pair1[0]
        else:
            new_bottom = pair2[0]

        if pair1[1] <= pair2[1]:
            new_top = pair2[1]
        else:
            new_top = pair1[1]

        return (new_bottom, new_top)

    # Containing
    elif pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
        # Then, pair2 should be erased from results list, or simply replace both pairs for one of the pairs, the
        # cointaining pair
        new_bottom = pair1[0]
        new_top = pair1[1]
        return (new_bottom, new_top)

    elif pair2[0] <= pair1[0] and pair2[1] >= pair1[1]:
        new_bottom = pair2[0]
        new_top = pair2[1]
        return (new_bottom, new_top)

    else:
        return False

"""
def my_fun(input_list):
"""


# Testing

my_example = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(my_fun(my_example))
