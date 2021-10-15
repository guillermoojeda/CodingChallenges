"""
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?

"""

myInt = 10101010

myInt2 = str(myInt)

myInt3 = ""

for i in myInt2:
    if i == "0":
        i = "1"
    else:
        i = "0"
    myInt3 = myInt3 + i

print(int(myInt3))

## Bonus ~~~

print(bin(int('11111111', 2) - int('10101010', 2))[2:])




