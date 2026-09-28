#Topic-7 — match-case


# Q50. Basic Menu

menu_number = int(input("Enter Number From 1 to 4 : "))
match menu_number:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Update")
    case 4:
        print("Delete")
    case _:
        print("Invalid Choice")

# Q51. Day Name Using match-case

day_number =int (input("Enter Day No. : "))
match day_number :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print ("Invaild User Input!")

# Q52. Calculator Using match-case

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
match operator:
    case "+":
        print("Result:", first_number + second_number)
    case "-":
        print("Result:", first_number - second_number)
    case "*":
        print("Result:", first_number * second_number)
    case "/":
        if second_number == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", first_number / second_number)
    case _:
        print("Invalid operator")

# Q53
 color = input("Signal colour:")
 match color:
     case "red":
        print("Stop")
    case "green":
        print("Go")
    case "yellow":
        print("Wait")
    case _:
        print("Invalid Signal")

# Q54
grade = input("Your Grade:")
match grade:
    case "A":
        print("Excellent Performance")
    case "B":
        print("Very Good Performance")
    case "C":
        print("Good Performance")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Failed")
    case _:
        print("Invalid Grade")

# Q55
code = int(input("Enter Service Code:"))
match code:
    case 1:
        print("Check Balance")
    case 2:
        print("Recharge")
    case 3:
        print("Data Usage")
    case 4:
        print("Customer Support")
    case _:
        print("Invalid Service")

# Q56
month = int(input("Month no.:"))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid Month")

# Q57
ext = input("Enter extension type:")
match ext:
    case "py":
        print("Python File")
    case "txt":
        print("Text File")
    case "pdf":
        print("PDF File")
    case "jpg":
        print("Image File")
    case _:
        print("Unknown File Type")
