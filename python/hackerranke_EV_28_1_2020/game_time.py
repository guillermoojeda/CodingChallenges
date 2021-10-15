#
#
# []

m = "02"



if len(m) == 2 and (m[0] == 0):
    m = m[1]

print(m[1])

print(m)


#!/bin/python3
import math
import os
import random
import re
import sys
import datetime
#
# Complete the 'game_time_with_minutes' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER start_h
#  2. INTEGER start_m
#  3. INTEGER end_h
#  4. INTEGER end_m
#
def game_time_with_minutes(start_h, start_m, end_h, end_m):
    d1 = datetime.timedelta(hours=1, minutes=2)
	d2 = datetime.timedelta(hours=4, minutes=5)
	result = str(d2 - d1)
	h, m = result.split(':')[:-1]
	# h, m, s = result.timedelta
	print('THE GAME LASTED {} HOUR(S) AND {} MINUTE(S)'.format(h,m))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    start_h = int(first_multiple_input[0])
    start_m = int(first_multiple_input[1])
    end_h = int(first_multiple_input[2])
    end_m = int(first_multiple_input[3])
    result = game_time_with_minutes(start_h, start_m, end_h, end_m)
    fptr.write(result + '\n')
    fptr.close()