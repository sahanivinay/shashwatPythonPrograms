import pandas as pd
file = 'Student.xlsx'
data = pd.read_excel(file)
print(data.head())
column = pd.read_excel(file,usecols=['Age'])
print(column)
