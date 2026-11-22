# # Level - 1 -------------


# # Q21. Print Numbers from 1 to N
# n=int(input())
# i=1
# while i<=n:
#     print(i)
#     i+=1

# # Q22. Print Numbers from N to 1
# n=int(input())
# while n>=1:
#     print(n)
#     n-=1

# # Q23. Print Even Numbers up to N
# n=int(input())
# i=2
# while i<=n:
#     print(i)
#     i+=2

# # Q24. Print Odd Numbers up to N
# n=int(input())
# i=1
# while i<=n:
#     print(i)
#     i+=2

# # Q25. Print Multiples of a Number
# k=int(input())
# n=int(input())
# i=k
# while i<=n:
#     print(i)
#     i+=k


# # Level - 2 -------------


# # Q26. Multiplication Table
# n=int(input())
# i=1
# while i<=10:
#     print(n,"x",i,"=",n*i)
#     i+=1

# # Q27. Count by a Given Step
# start=int(input())
# step=int(input())
# i=1
# while i<=5:
#     print(start)
#     start+=step
#     i+=1

# # Q28. Sum of Numbers from 1 to N
# n=int(input())
# i=1
# total=0
# while i<=n:
#     total+=i
#     i+=1
# print(total)

# # Q29. Sum of Even Numbers up to N
# n=int(input())
# i=2
# total=0
# while i<=n:
#     total+=i
#     i+=2
# print(total)

# # Q30. Sum of Odd Numbers up to N
# n=int(input())
# i=1
# total=0
# while i<=n:
#     total+=i
#     i+=2
# print(total)


# # Level - 3 ------------------


# # Q31. Calculate the Total Cost
# price=int(input())
# quantity=int(input())
# total=0
# i=1
# while i<=quantity:
#     total+=price
#     i+=1
# print(total)

# # Q32. Calculate Total Savings
# daily_saving=int(input())
# days=int(input())
# total=0
# i=1
# while i<=days:
#     total+=daily_saving
#     i+=1
# print(total)

# # Q33. Calculate a Number Raised to a Power
# base=int(input())
# power=int(input())
# result=1
# i=1
# while i<=power:
#     result*=base
#     i+=1
# print(result)

# # Q34. Calculate Factorial
# n=int(input())
# factorial=1
# i=1
# while i<=n:
#     factorial*=i
#     i+=1
# print(factorial)

# # Q35. Find the Sum from START to END
# start=int(input())
# end=int(input())
# total=0
# while start<=end:
#     total+=start
#     start+=1
# print(total)


# # Level - 4 -------------------


# # Q36. Count Down by Two
# n=int(input())
# while n>=2:
#     print(n)
#     n-=2

# # Q37. Repeatedly Divide by Two
# n=int(input())
# while n>0:
#     n//=2
#     print(n)

# # Q38. Count How Many Steps Are Needed
# n=int(input())
# steps=0
# while n>0:
#     n-=3
#     steps+=1
# print(steps)

# # Q39. Save Until the Target Is Reached
# saved=int(input())
# daily_amount=int(input())
# target=int(input())
# days=0
# while saved<target:
#     saved+=daily_amount
#     days+=1
# print(days)

# # Q40. Print a Number Sequence in Reverse Steps
# start=int(input())
# step=int(input())
# while start>=0:
#     print(start)
#     start-=step