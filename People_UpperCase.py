# Creating an empty list
People = []
# Taking the input value of N
N = int(input("Enter the Number of People: "))

# For loop to iterate till N range
for i in range(0,N):
    # Taking input name in List
    name = str(input())
    # Inserting the name into list using append method
    People.append(name)

# Printing the name of the people in list
print("People in list: ",People)

# Converting to uppercase
upper_case = [x.upper() for x in People]

# Printing the names in uppercase
print("Uppercase People: ",upper_case)