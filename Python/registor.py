# Input the Name,Age, and Basic Salary of an employee.
# Calculate the total salary of an employee adding 10% DA and 15% HRA to the Basic Salary.

name=input("Write your name:")
age=input('your age:')
Basic=int(input("Enter your basic salary:"))
da=(Basic*10/100)
hra=(Basic*15/100)
print("Name:",name)
total_salary=(Basic+da+hra)
print("Name:",name)
print("Age:",age)
print("DA:",da)
print("HRA:",hra)
print("Basic salary:",Basic)
print("Total salary:",total_salary)