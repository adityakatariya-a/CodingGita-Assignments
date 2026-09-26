#Q-9 -----------

num = int(input("Enter an Integer: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

#Q-10 -----------

marks = int(input("Enter Marks: "))
if marks>=40:
    print("Pass")
else:
    print("Fail")

#Q-11 -----------

age = int(input("Enter Age: "))
if age>=18:
    print("Adult")
else:
    print("Minor")

#Q-12 -----------

num = int(input("Enter an Integer: "))
if num>0:
    print("Positive")
else:
    print("Non-positive")

#Q-13 -----------

num = int(input("Enter an Integer: "))
if num%3==0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")

#Q-14 -----------

correct_password = "python123"
password = input("Enter Password: ")
if password==correct_password:
    print("Login Successful")
else:
    print("Invalid Password")

#Q-15 -----------

correct_username = "admin"
username=input("Enter username : ")
if correct_username==username:
    print("Welcome Admin")
else:
    print("Invalid Username")

#Q16. Greater Between Two Numbers

num1, num2 = (int, input().split(","))
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("Both are Equal")

# Q17. Hot or Comfortable

temperature= int(input("Enter Temperature : "))
if temperature > 30:
    print("Hot")
else:
    print("Comfortable")

#Q18. Shopping Discount Eligibility

shopping_amount=int(input("Enter Shopping Amount : "))
if shopping_amount>=5000:
    print("Discount Available")
else:
    print("No Discount")