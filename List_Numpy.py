# Importing the numpy module
import numpy as np

# Creating array using arange() method arange(start,stop,step)
arangeMethodArray = np.arange(1,51,2)
# Sorting the above array using sort() method
sortedArrayArange= np.sort(arangeMethodArray)
# Printing the original array
print("Original Arrange Array \n",arangeMethodArray)
# Printing the original array
print("Sorted Array\n",sortedArrayArange)

# Creating array using linspace() method linspace(start,stop)
linspaceMethodArray = np.linspace(1,10)
# Sorting the above array using sort() method
sortedArrayLinspace = np.sort(linspaceMethodArray)
# Printing the original array
print("Original Linspace Array \n",linspaceMethodArray)
# Printing the original array
print("Sorted Array\n",sortedArrayLinspace)