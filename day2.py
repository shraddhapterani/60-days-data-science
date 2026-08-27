# Function to calculate average marks
def calculate_average(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return average

# Function to classify grade 
def classify_grade(average):
    if average >= 75:
        return "Distinction"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"

# Take input
num_subjects = int(input("Enter number of subjects: "))

#Use a loop to collect marks for each subject
marks_list = []
for i in range(num_subjects):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    marks_list.append(marks)

#Calculate average using function
average_marks = calculate_average(marks_list)

#Classify grade using function
result = classify_grade(average_marks)

#Output
print("\n--- Result ---")
print(f"Marks entered: {marks_list}")
print(f"Average: {average_marks:.2f}")
print(f"Result: {result}")