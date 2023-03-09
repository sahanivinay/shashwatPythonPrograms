# Pointer to open the file in write mode
writing_file = open("a.out","w")
# Taking user input for the content the file
inputFile1 = input("----------------------- Enter Some Text into your file ------------------------\n")
# Writing the user content into the file using write() method
writing_file.write(inputFile1)
# Closing the file pointer (mandatory to close file once opened)
writing_file.close()

# Pointer to open the file in read mode
reading_file = open("a.out","r")
# Reading the contents of the file using readline() method
readFile = reading_file.readline()
# Closing the file pointer (mandatory to close file once opened)
reading_file.close()
# Printing the content of the file
print("\n\n------------------------------ Your File Content ------------------------------\n\n",readFile)
"""
append_file = open("a.out","a")
updateFile = input("Do you want to update your file? (Y/N): ")
if updateFile == 'Y':
    inputFile2 = input("\n--------------------- Enter Some Text Update your file ---------------------\n\n")
    append_file.write(inputFile2)
    append_file.close()
    reading_file = open("a.out", "r")
    readFile = reading_file.readline()
    reading_file.close
    print("\n\n\n----------------------- Your Updated File Content ------------------------\n\n", readFile)
else:
    exit()"""

