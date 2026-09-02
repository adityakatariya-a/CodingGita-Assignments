# TOPIC 1 : TYPE CASTING 

# Question 1 -----------------------------------------------------------------------------------------------

age = "25"
age=int(age)

print(age)
print(type(age))

# Question 2 -----------------------------------------------------------------------------------------------

marks="75.5"
marks=float(marks)

print(marks)
print(type(marks))

# Question 3 -----------------------------------------------------------------------------------------------

number = 50
number = float(number)

print(number)
print(type(number))

# Question 4 -----------------------------------------------------------------------------------------------

marks = 85.9
marks = int(marks)

print(marks)
print(type(marks))

# Question 5 -----------------------------------------------------------------------------------------------

roll_number=101
roll_number=str(roll_number)

print(roll_number)
print(type(roll_number))

# Question 6 -----------------------------------------------------------------------------------------------

age = "18"
age=int(age)

print(age)
print(type(age))

#------------------------

marks="92.5"
marks=float(marks)

print(marks)
print(type(marks))

#-------------------------

roll_number=100
roll_number=str(roll_number)

print(roll_number)
print(type(roll_number))

# ------------------------

marks = 45.8
marks = int(marks)

print(marks)
print(type(marks))

# Question 7 -----------------------------------------------------------------------------------------------

a = "20"
b = int(a)

c = 10.8
d = int(c)

e = 25
f = str(e)

print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))

# Question 8 -----------------------------------------------------------------------------------------------

age = 19
new_age = age + 1

print("Age:", new_age)
#the value of the variable "age" is in string datatype

# Question 9 -----------------------------------------------------------------------------------------------

marks="85"
marks=int(marks)
marks += 5

print("Final marks:", marks)

# Question 10 -----------------------------------------------------------------------------------------------

price="1499.50"
delivery_charges=99.50

price=float(price)
price += delivery_charges

print("Toatal amount:" , price)


# TOPIC 2 : ARITHMETIC OPERATORS

# Question 11 -----------------------------------------------------------------------------------------------

a=20
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Question 12 -----------------------------------------------------------------------------------------------

a = 17
b = 5

print(a / b) # the output is 3.4
print(a // b) # the output is 3
print(a % b) # the output is 2

# a / b performs normal division, so it returns the floating-point result 3.4.
#a // b performs floor division, so it returns only the whole number 3, while a % b returns the remainder after division, which is 2.

# Question 13 -----------------------------------------------------------------------------------------------

result = 10 + 5 * 2
print(result)

# to being addition first

result = (10 + 5) * 2
print(result)

# Question 14 -----------------------------------------------------------------------------------------------

result = 20 - 4 * 3 + 2
print(result) #output is 10

# after rewrite it 

result = (20 - (4 * 3)) + 2
print(result) 

# Question 15 -----------------------------------------------------------------------------------------------

print(2 ** 3) # --> 8
print(3 ** 2) # --> 9
print(10 ** 2) # -> 100

# area of the square

side=5
area_of_square= 5**2

print(area_of_square)

# Question 16 -----------------------------------------------------------------------------------------------

notebook = 80
pen = 20
pencil = 10
total_amount= notebook+pen+pencil

print(total_amount)

# Question 17 -----------------------------------------------------------------------------------------------

notebook = 50
pen = 15
calculator =500

notebook_cost= 3*notebook
pen_cost= 2*pen
calculator_cost= 1*calculator
total_bill= notebook_cost + pen_cost + calculator_cost

print("Notebook cost:", notebook_cost)
print("Pen cost:", pen_cost)
print("Calculator cost:", calculator_cost)
print("Total bill:", total_bill)

# Question 18 -----------------------------------------------------------------------------------------------

total_students= 47

complete_groups= 47//5
student_left_over= 47%5

print("Complete groups:", complete_groups)
print("students Left:", student_left_over)

# Question 19 -----------------------------------------------------------------------------------------------

python= 85
mathematics= 78
physics= 92

total_marks= python + mathematics + physics
average_mrks= total_marks/3

print("Total marks :" , total_marks)
print( "average marks :" , average_mrks)

# Question 20 -----------------------------------------------------------------------------------------------

English = 78
Mathematics = 85
Python = 92
Physics = 81
Chemistry = 74

#Each subject is out of 100.

total_marks= English + Mathematics + Python + Physics + Chemistry
percentage= (total_marks/500)*100

print(total_marks)
print(percentage)