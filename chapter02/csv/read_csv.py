#-*- coding: utf-8 -*-
#Edited by bighead 18-12-29

import csv

file_name = "ch02-data.csv"

try:
    with open(file_name, 'r')as f:
        reader = csv.reader(f)
        header = reader.next()
        data = [row for row in reader]
except csv.Error as e:
    print("Error reading csv file at line %s: %s", (reader.line_num, e))

print(reader)
print(header)
print("=======")
print(data)
