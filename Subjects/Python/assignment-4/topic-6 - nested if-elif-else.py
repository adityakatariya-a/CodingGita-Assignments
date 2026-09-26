    #   Topic-6 — Nested if-elif-else


# Q44. Greatest of Three Numbers

a = int(input("Enter integer A : "))
b = int(input("Enter integer B : "))
c = int(input("Enter integer C : "))
if a>b and a>c:
    print("A is Greatest")
elif b>c:
    print("B is Greatest")
elif c>b and c>a:
    print("C is Greatest")
elif a==b and a>c:
    print("A and B are Equal and Greatest")
elif a==c and a>b:
    print("A and C are Equal and Greatest")
elif b==c and b>c:
    print("B and C are Equal and Greatest")
else:
    print("All are Equal")

# Q45. Student Result with Grade

marks=int(input("Enter Marks : "))
attendance=int(input("Enter attendance : "))
if attendance>=75:
    if marks>=90:
        print("Grade A")
    elif marks>=75:
        print("Grade B")
    elif marks>=60:
        print("Grade C")
    elif marks>=40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")

# Q46. Employee Bonus

salary = int(input("Enter salary : "))
performance_rating = int(input("Enter performance rating : "))
if salary >=30000:
    if performance_rating==5:
       print("Bonus: 20%") 
    elif performance_rating==4:
        print("Bonus: 15%")
    elif performance_rating==3:
        print("Bonus: 10%") 
    elif performance_rating==2:
        print("Bonus: 5%")  
    else:
        print("Not Eligible for Bonus") 
else:
    print("Not Eligible for Bonus")  

# Q47. Bus Ticket Category 

age = int(input("Enter age : "))
distance = int(input("Enter Distance : "))
if age >= 60:
    print("Senior")
elif age >=5:
    print("Regular", end=" - ")
    if distance>10:
        print("Long Distance")
    else:
        print("Short Distance")
else:
    print("Free")

# Q48. Product Purchase Validation

product_stock = int(input("Enter product stock : "))
payment_status = (input("Enter payment status : "))
if product_stock>0:
    if payment_status ==  "paid":
        print(" Order Confirmed")
    elif payment_status == "pending":
        print("Payment Pending")
    else: 
        print("Invalid Payment Status")
else:
    print("Out of Stock") 

# Q49. Travel Ticket Validation

age = int(input("Enter Age : "))
ticket_type= (input("Enter ticket type : "))
if age >= 60:
    print("Free Travel")
elif age>=5:
    print("Regular Passenger")
    if ticket_type== "AC":
        print("AC Ticket")
    elif ticket_type== "Sleeper":
        print("Sleeper Ticket")
    else:
        print(" Invalid Ticket Type")
else:
    print("Free Travel")
