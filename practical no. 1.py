#Student Data System
#Demonstrate python building blocks , data types,and I/O

print("===Student Data System===")

#input section (user provide data)
name=input("Enter student name:") #str
roll_no= int(input("Enter your roll_no:"))
age = int(input("Enter age:"))
marks = float(input("Enter marks:"))
is_pass = marks>=40

#Processing section
percentage = (marks/100)*100
#output section
print("\n===Student Details===")
print("Name:",name)
print("Roll Number:",roll_no)
print("age:",age)
print("marks:",marks)
print("Percentage:",percentage)
print("Result:","Pass"if is_pass else "fail")

#Display data type (to understanding building blocks)
print("\n=== Data Types Used ===") 
print("Type of name:", type(name))
print("Type of roll_no:", type(roll_no))
print("Type of age:", type(age))
print("Type of marks:", type(marks))
print("Type of is_pass:", type(is_pass))
