'''
import csv

filtered_students = []

with open("student.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if (row["class"] in ["Four", "Five"] and
            float(row["mark"]) > 70 and
            row["gender"].lower() == "male"):
            filtered_students.append(row)

print(f"{'id':<5} {'name':<15} {'class':<10} {'mark':<6} {'gender':<10}")

for student in filtered_students:
    print(f"{student['id']:<5} {student['name']:<15} {student['class']:<10} {student['mark']:<6} {student['gender']:<10}")
'''

import pandas as pd
dt=pd.read_csv('student.csv')
result = dt[((dt['class'] == 'Four') | (dt['class'] == 'Five')) & (dt['mark'] > 70) & (dt['gender'] == 'male')]
print(result)




