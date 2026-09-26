# Topic-4 — Logical Conditions


#Q29. College Admission Eligibility


marks=int(input("Enter Marks : "))
attendance=int(input("Enter attendance : "))
if marks>=60:
    if attendance>=75:
        print("Eligible")
    else :
        print ("Not Eligible")
else :
    print ("Not Eligible")

# Q30. Scholarship Eligibility

marks=int(input("Enter Marks : "))
family_income=int(input("Enter family income : "))
if marks>=85:
    if family_income<=300000:
        print("Scholarship Available")
    else:
        print("No Scholarship")
else:
    print("No Scholarship")


#Q31. Weekend Check

day =input("Enter a week day")
if (day == "Saturday" or day == "Sunday"):
    print("Weekend")
else:
    print("Weekday")

#Q32. Online Exam Access

username="student"
password="python123"
enter_username=input("Enter Username : ")
enter_password=input("Enter Password : ")
if username == enter_username :
    print("Access Granted")
else:
    print("Access Denied")

# Q33. Delivery Availability

City=input("Enter City Name : ")
if (City == "Ahmedabad" or City == "Gandhinagar"):
    print("Access Granted")
else:
    print("Access Denied")

#Q34. Number Range Check

integer=input("Enter Integer : ")
if 50 >= integer >= 10 :
    print("Inside Range")
else:
    print("Outside Range")

# Q35. Secure Transaction

amount = int(input("Enter Amount : "))
OTP  = "1234"
otp = (input("Enter OTP : "))
if amount <= 50000:
    if otp == OTP :
        print("Transaction Approved")
    else:
        print("Transaction Declined")
else:
    print("Transaction Declined")
