# # Level - 1 ----------------


# # Q41. Count the Digits
# n=int(input())
# count=0
# if n==0:
#     count=1
# while n>0:
#     count+=1
#     n//=10
# print(count)

# # Q42. Find the Sum of Digits
# n=int(input())
# total=0
# while n>0:
#     digit=n%10
#     total+=digit
#     n//=10
# print(total)

# # Q43. Reverse a Number
# n=int(input())
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n//=10
# print(reverse)

# # Q44. Find the Product of Digits
# n=int(input())
# product=1
# if n==0:
#     product=0
# while n>0:
#     digit=n%10
#     product*=digit
#     n//=10
# print(product)

# # Q45. Print Digits from Right to Left
# n=int(input())
# while n>0:
#     digit=n%10
#     print(digit)
#     n//=10


# # Level - 2 ----------------------


# # Q46. Find the First and Last Digit
# n=int(input())
# last=n%10
# while n>=10:
#     n//=10
# first=n
# print("First digit:",first)
# print("Last digit:",last)

# # Q47. Count Even Digits
# n=int(input())
# count=0
# if n==0:
#     count=1
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         count+=1
#     n//=10
# print(count)

# # Q48. Count Odd Digits
# n=int(input())
# count=0
# while n>0:
#     digit=n%10
#     if digit%2!=0:
#         count+=1
#     n//=10
# print(count)

# # Q49. Find the Sum of Even Digits
# n=int(input())
# total=0
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         total+=digit
#     n//=10
# print(total)

# # Q50. Find the Largest Digit
# n=int(input())
# largest=0
# while n>0:
#     digit=n%10
#     if digit>largest:
#         largest=digit
#     n//=10
# print(largest)

# # Q51. Find the Smallest Digit
# n=int(input())
# smallest=9
# if n==0:
#     smallest=0
# while n>0:
#     digit=n%10
#     if digit<smallest:
#         smallest=digit
#     n//=10
# print(smallest)


# # Level - 3 ----------------


# # Q52. Check Whether a Number Is a Palindrome
# n=int(input())
# temp=n
# reverse=0
# while temp>0:
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp//=10
# if n==reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# # Q53. Count How Many Times a Digit Appears
# n=int(input())
# d=int(input())
# count=0
# if n==0 and d==0:
#     count=1
# while n>0:
#     digit=n%10
#     if digit==d:
#         count+=1
#     n//=10
# print(count)

# # Q54. Check Whether All Digits Are the Same
# n=int(input())
# digit=n%10
# same=True
# while n>0:
#     current=n%10
#     if current!=digit:
#         same=False
#     n//=10
# if same:
#     print("Yes")
# else:
#     print("No")

# # Q55. Compare the Sum of First and Last Digits with the Middle Digits' Sum
# n=int(input())
# last=n%10
# temp=n
# middle_sum=0
# while temp>=10:
#     digit=temp%10
#     middle_sum+=digit
#     temp//=10
# first=temp
# middle_sum-=last
# print("First and last digits sum:",first+last)
# print("Middle digits sum:",middle_sum)


# # Level - 4 ----------------


# # Q56. Print Factorial Values from 1! to N!
# n=int(input())
# i=1
# factorial=1
# while i<=n:
#     factorial*=i
#     print(factorial)
#     i+=1

# # Q57. Check Whether a Number Is a Factorial Value
# n=int(input())
# i=1
# factorial=1
# found=False
# while factorial<=n:
#     if factorial==n:
#         found=True
#     i+=1
#     factorial*=i
# if found:
#     print("Yes")
# else:
#     print("No")

# # Q58. Find the Largest Factorial Not Greater Than N
# n=int(input())
# i=1
# factorial=1
# while factorial<=n:
#     result=factorial
#     i+=1
#     factorial*=i
# print(result)