# Topic-3 — if-elif-else

#Q19. Grade Calculator

Marks=int(input("Enter Your Marks : "))
if Marks>=90:
    print("Grade A")
elif Marks>=80:
    print("Grade B")
elif Marks>=70:
    print("Grade C")
elif Marks>=60:
    print("Grade D")
else:
    print("Grade F")

#Q20. Temperature Category

temperature= int(input("Enter Temperature : "))
if temperature > 40:
    print("Very Hot")
elif 39>=temperature>=30:
    print("Hot")
elif 29>=temperature>=20:
    print("Warm")
else:
    print("Cold")


#Q21. Traffic Signal

color=input("Traffic Colour : ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid Signal")

#Q22. Electricity Usage Category

electricity_units=int(input("Enter Electricity Units : "))
if electricity_units>500:
    print("Very High Usage")
elif electricity_units>=300:
    print("High Usage")
elif electricity_units>=100:
    print("Medium Usage")
else:
    print("Low Usage")

#Q23. Movie Ticket Category

age = int (input("Enter age : "))
if age >=60:
    print("Senior Ticket")
elif age >=13:
    print("Regular Ticket")
elif age >=5:
    print("Child Ticket")
else:
    print("Free Ticket")

# Q24. BMI Category

BMI = float(input("Enter BMI : "))
if BMI>=30:
    print("Obese")
elif BMI>=24.9:
    print("Overweight")
elif BMI>=18.5:
    print("Normal")
else:
    print("Underweight")

# Q25. Month Days

month_number= int(input("Enter month number : " ))
if month_number == (1 or 3 or 5 or 7 or 8 or 10 or 12):
    print("31 Days")
elif month_number == (4 or 6 or 9 or 11):
    print("30 Days")
elif month_number == 2  :
    print(" 28 or 29 Days")
else:
    print("Invalid Month")

# Q26. Simple Calculator

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
	print("Result:", first_number + second_number)
elif operator == "-":
	print("Result:", first_number - second_number)
elif operator == "*":
	print("Result:", first_number * second_number)
elif operator == "/":
	if second_number == 0:
		print("Cannot divide by zero")
	else:
		print("Result:", first_number / second_number)
else:
	print("Invalid operator")

# Q27. Day Number

week=int(input("Enter Day Number : "))
if week == 1 :
    print("Monday!")
elif week == 2 :
    print("Tuesday!")
elif week == 3 :
    print("Wednesday!")
elif week == 4 :
    print("Thursday!")
elif week == 5 :
    print("Friday!")
elif week == 6 :
    print("Suesday!")
elif week == 7 :
    print("Sunday!")
else :
    print("INVALID DAY NUMBER!")

# Q28. Performance Level

score=int(input("Enter Your Score : "))
if score>=90:
    print("Excellent")
elif score>=75:
    print("Very Good")
elif score>=60:
    print("Good")
elif score>=40:
    print("Average")
else:
    print("Needs Improvement")