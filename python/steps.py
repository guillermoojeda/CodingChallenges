# Given a staircase with n steps, write a function called num_ways(n), which returns the amount of possibles ways
# you can go from the bottom to the top (example:, one way is one step at the time, other way is 2 steps, then 3, then
# and  so on...
# E.G. For a n=2, there are only 2 ways of getting to the top: one step, and one step after that, OR two steps
# in one same move.

# Part 2: The same, but this time you are given X, which is a set of possible amounts of steps at a time you can "jump".

def num_ways(n):
    for i in range(n):
        if n