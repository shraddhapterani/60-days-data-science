# day3.py
import csv

# 1. Read the CSV file and count grade frequency
grade_count = {}  # dictionary to store counts, e.g. {"Pass": 3, "Fail": 1}

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)  # reads each row as a dictionary
    for row in reader:
        grade = row["grade"]
        if grade in grade_count:
            grade_count[grade] += 1
        else:
            grade_count[grade] = 1

# 2. Write summary to a new output file
with open("summary.txt", "w") as output_file:
    output_file.write("--- Grade Summary ---\n")
    for grade, count in grade_count.items():
        output_file.write(f"{grade}: {count}\n")

# 3. Also print to screen so we can see it
print("Summary written to summary.txt")
print(grade_count)