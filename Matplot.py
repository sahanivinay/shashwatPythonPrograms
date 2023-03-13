# Importing required module
import matplotlib.pyplot as plt
import random

# Creating empty list for X - axis
x = []
# Creating empty list for Y - axis
y = []
# Taking input for number of elements
number = int(input("Enter the number of elements: "))
print("Enter the x-values")

# Function to generate y-values when x values are given
def plotGraph():
    for i in range(0, number):
        x_values = int(input())
        if x_values > 100:
            break
        x.append(x_values)

    for i in range(0, number):
        y_values = random.randint(1, 100)
        y.append(y_values)
    # Corresponding x axis values
    print("X axis: ", x)
    # Corresponding y axis values
    print("Y axis: ", y)


    # Plotting the points
    plt.plot(x, y, color='red', linewidth=2)

    # Naming the x axis
    plt.xlabel('x - axis')
    # Naming the y axis
    plt.ylabel('y - axis')

    # Giving a title to my graph
    plt.title('My first graph using matplotlib')

    # Function to show the plot
    plt.show()

plotGraph()