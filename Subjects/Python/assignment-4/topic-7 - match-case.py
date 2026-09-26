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