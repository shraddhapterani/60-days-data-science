#user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary_input = input("Enter your monthly salary: ")
monthly_salary = float(salary_input.replace(",", ""))  # remove commas before converting

#Calculate yearly salary
yearly_salary = monthly_salary * 12

#Store data in a dictionary
person_data = {
    "name": name,
    "age": age,
    "monthly_salary": monthly_salary,
    "yearly_salary": yearly_salary
}

#Output the result
print("\n--- Your Data ---")
print(person_data)