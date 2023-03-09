# Creating an list
list = [10,20,30,40,50,60,70,80,90,100]

# Printing the original list
print("Original List: ",list)

# This line prints element from 0th Index to fifth element and takes  2 steps
print("This line prints element from 0th Index to fifth element and takes  2 steps\n")
print(list[0:5:2])

# This line prints element from 0th Index to -1 (i.e. last element)
print("This line prints element from 0th Index to -1 (i.e. last element)\n")
print(list[0:-1])

# This line prints element from 0th Index to the last element as Nth index is not specified
print("This line prints element from 0th Index to the last element as Nth index is not specified\n")
print(list[0:])

# This line prints element from -1 Index to 10th elements (i.e. -1 = Nth index)
print("This line prints element from -1 Index to 10th elements (i.e. -1 = Nth index)\n")
print(list[-1:10])

# This line prints element from 5th Index to 10th element and takes one step
print("This line prints element from 5th Index to 10th element and takes one step\n")
print(list[5:10:1])
