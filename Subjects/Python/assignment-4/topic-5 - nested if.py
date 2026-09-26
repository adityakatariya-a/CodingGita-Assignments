#      Topic-5 — Nested if


# Q36. Login with Role

username="admin"
password="admin123"
enter_username=input("Enter Username : ")
if username == enter_username :
    enter_password=input("Enter Password : ")
    if password == enter_username :
        print("Access Granted")
    else :
        print("Access Denied")
else:
    print("Access Denied")

# Q37. Driving License Eligibility

age = int(input("Enter Age : "))
if age == 18 :
    test_status = input("Enter Test Status : ")
    if test_status=="Pass":
        print ("License Approved")
    else:
        print ("Test Not Passed")
else:
    print ("Age Not Eligible")


# Q38. ATM Withdrawal

account_balance=int(input("Account Balance : "))
withdrawal_balance=int(input("Withdrawal Balance : "))
if account_balance>=withdrawal_balance:
    if withdrawal_balance % 100 == 0 :
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")

#Q39. Exam Result with Attendance

marks = int(input("Enter Marks : "))
attendance = int(input("Enter Attendance : "))
if attendance >=75:
    if marks >=40:
        print("pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")

# Q40. Bank Account Verification

account_balance=input("Enter account type : ")
balance=int(input("Enter balance : "))
if account_balance =="savings":
    if balance>=100:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")

# Q41. Online Shopping Eligibility

order_amount = int(input("Enter Order amount : "))
payment_method = (input("Enter Payment method : "))

if order_amount>=500:
    if payment_method == "card":
        print("Card Payment Accepted")
    elif payment_method == "upi":
        print("UPI Payment Accepted") 
    else:
        print("Unsupported Payment Method") 
else:
    print("Minimum Order Amount Not Reached") 

# Q42. Hostel Room Allocation

year_of_study = int(input("Enter year of study: "))
attendance = int(input("Enter attendance: "))
if (year_of_study == 2 or year_of_study == 3 or year_of_study == 4 ):
    if attendance >=75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")

# Q43. Internet Plan Upgrade

current_plan = (input("Enter current plan : "))
monthly_usage = int(input("Enter monthly usage : "))
if current_plan == "basic":
    if monthly_usage>100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")

