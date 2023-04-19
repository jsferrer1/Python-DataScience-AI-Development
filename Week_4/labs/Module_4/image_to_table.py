# read csv file student_grades.csv
# create a dataframe from the table

# install pandas
# pip install pandas

import pandas as pd

# read csv file student_grades.csv
df = pd.read_csv('student_grades.csv')

# convert dataframe to dictionary
# dictionary should be in this format: x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 'Salary':[100000, 80000, 50000, 60000]}
d = df.to_dict('list')

x = {'Student': ['David', 'Samuel', 'Terry', 'Evan'],
     'Age': [27, 24, 22, 32],
     'Country': ['UK', 'Canada', 'China', 'USA'],
     'Course': ['Python',
                'Data Structures',
                'Machine Learning',
                'Web Development'],
     'Marks': [85, 72, 89, 76]}

# convert dataframe to list
l = df.values.tolist()

# display the dataframe
print(df)

# install matplotlib
# pip install matplotlib
