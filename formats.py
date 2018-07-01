# File: formats.py
# Description: Examples on how to process csv files in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Examples on how to process csv files in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Processing_csv_files_in_Python (date of access: XX.XX.XXXX)



# Working with text files created in different formats

import csv

with open('example.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# Adding more information in the csv file
students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open('example.csv', 'a') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in students:
        writer.writerow(row)


# Implementing the task
# Reading large file with data in format of csv
# The task is to find the 'Primary type' which is met maximum times in 2015 year

# Creating a set for storing types by unique name
types_set = set()

# Creating a list for writing all meat types including the repeated ones
types_list = []

# Reading and processing file csv and extracting needed data
with open('data.csv') as f:
    reader = csv.reader(f)
    # Reading only specific columns we need
    for row in reader:
        date_time = row[2].split(' ')  # Reading column Date and splitting by gap date and time
        date = date_time[0].split('/')  # Splitting day/month/year by '/'

        if len(date) == 3:  # Eliminating processing the first row with names of the columns
            # Extracting only year from the date
            year = date[2]
            # Extracting all met types from column 'Primary Type' only for year of 2015
            if year == '2015':
                # Adding all met types into the list with repeated ones
                types_list += [row[5]]

# Fulling the set with the types from the list but it'll save only unique ones
types_set = set(types_list)

# Calculating how many times each unique type is met in the list
# And defining the maximum one at the same time
m = 0
m_type = ''
for x in types_set:
    n = types_list.count(x)
    if n > m:
        m = n
        m_type = x

# Showing the result - type and number of time it was met
print(m_type, str(m))
