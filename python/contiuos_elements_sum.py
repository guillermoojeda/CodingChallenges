"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

myList = [1, 2, 3, 4, 5]

myResult = []
for i in range(0, len(myList)):
    mySum = 0
    myElements = []
    while mySum < 9:
        for j in range(i, len(myList)):
            mySum = mySum + myList[j]
            myElements.append(myList[j])
            if mySum == 9:
                myResult.append(myElements)
                break
            elif mySum > 9:
                break

print(myResult)
