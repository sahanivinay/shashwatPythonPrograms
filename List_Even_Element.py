# Creating an empty list
a = []
# Taking input value of N
N = int(input("Enter the number of elements: "))

# For loop to iterate till N range
for i in range(0,N):
    # Taking input elements in List
    Element = int(input())
    # Inserting the element into list using append method
    a.append(Element)

# Printing the list values
print("List Elements: ",a)

# Creating an empty list
b = []
# Loop to iterate through list a
for even in a:
    # If statement to find even number in list
    if even % 2 == 0:
        # Inserting the even element into new list b using append method
        b.append(even)

# Printing the even elements in list
print("Even Elements in list: ",b)

