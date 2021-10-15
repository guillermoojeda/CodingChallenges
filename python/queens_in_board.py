#  You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
#  where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row,
#  column, or diagonal.

N = 5
myBoard = []

#Creating board
for i in range(N):
    myRow = []
    for i in range(N):
        myRow.append(" ")
    myBoard.append(myRow)

#moves list for queen
dir1 = []
dir2 = []
dir3 = []
dir4 = []

for i in range(-(N-1), N):
    dir1.append([i, 0])
    dir2.append([i, i])
