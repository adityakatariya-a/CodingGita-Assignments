# # Part A --------------


# # Q79. Check Whether a Number Is Prime

# isprime = True
# fact = 2
# num = int(input("Enter a number : "))
# while fact < num :
#     if num <= 1:
#         isprime = False
#     else:
#         if num % fact == 0:
#             isprime = False
#             break
#         else:
#             fact += 1
#             continue
# if isprime :
#     print("Number is prime.")
# else:
#     print("Number is not prime.")


# # Q80. Find HCF (GCD)

# a = int(input())
# b = int(input())

# while b != 0:
#     remainder = a % b
#     a = b
#     b = remainder

# print(a)


# # Q81. Find LCM

# a = int(input())
# b = int(input())

# if a > b:
#     lcm = a
# else:
#     lcm = b

# while True:
#     if lcm % a == 0 and lcm % b == 0:
#         break
#     lcm += 1

# print(lcm)


# # Q82. Check Whether a Number Is Perfect

# n = int(input())

# i = 1
# total = 0

# while i < n:
#     if n % i == 0:
#         total += i
#     i += 1

# if n > 1 and total == n:
#     print("Perfect")
# else:
#     print("Not Perfect")


# # Q83. Check Whether a Number Is Strong

# n = int(input())

# temp = n
# total = 0

# factorials = {
#     0: 1, 1: 1, 2: 2, 3: 6, 4: 24,
#     5: 120, 6: 720, 7: 5040,
#     8: 40320, 9: 362880
# }

# while temp > 0:
#     digit = temp % 10
#     total += factorials[digit]
#     temp //= 10

# if total == n:
#     print("Strong")
# else:
#     print("Not Strong")


# # Q84. Check Whether a Number Is Armstrong

# n = int(input())

# temp = n
# digits = 0

# if temp == 0:
#     digits = 1

# while temp > 0:
#     digits += 1
#     temp //= 10

# temp = n
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total += digit ** digits
#     temp //= 10

# if total == n:
#     print("Armstrong")
# else:
#     print("Not Armstrong")


# # Q85. Convert Decimal to Binary

# n = int(input())

# binary = 0
# place = 1

# if n == 0:
#     binary = 0

# while n > 0:
#     remainder = n % 2
#     binary += remainder * place
#     place *= 10
#     n //= 2

# print(binary)


# # Q86. Find Sum of Divisors

# n = int(input())

# i = 1
# total = 0

# while i <= n:
#     if n % i == 0:
#         total += i
#     i += 1

# print(total)


# # Part B --------------------


# # Q87. Print a Number Triangle
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     print()
#     i+=1

# # Q88. Print a Hollow Rectangle
# r=int(input())
# c=int(input())
# i=1
# while i<=r:
#     j=1
#     while j<=c:
#         if i==1 or i==r or j==1 or j==c:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     print()
#     i+=1

# # Q89. Print a Right-Aligned Triangle
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(" ",end=" ")
#         j+=1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

# # Q90. Print a Multiplication Grid
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(i*j,end=" ")
#         j+=1
#     print()
#     i+=1


# # Part C -------------------


# # Q91. Print the Fibonacci Series up to a Limit
# n=int(input())
# a=0
# b=1
# if n>=0:
#     print(0,end=" ")
# while b<=n:
#     print(b,end=" ")
#     a,b=b,a+b
# print()

# # Q92. Print All Prime Numbers up to N
# n=int(input())
# i=2
# while i<=n:
#     j=2
#     prime=True
#     while j<i:
#         if i%j==0:
#             prime=False
#             break
#         j+=1
#     if prime:
#         print(i,end=" ")
#     i+=1
# print()

# # Q93. Print All Armstrong Numbers up to N
# n=int(input())
# num=0
# while num<=n:
#     temp=num
#     digits=0
#     if temp==0:
#         digits=1
#     while temp>0:
#         digits+=1
#         temp//=10
#     temp=num
#     total=0
#     while temp>0:
#         digit=temp%10
#         power=1
#         i=1
#         while i<=digits:
#             power*=digit
#             i+=1
#         total+=power
#         temp//=10
#     if total==num:
#         print(num,end=" ")
#     num+=1
# print()

# # Q94. Print All Perfect Numbers up to N
# n=int(input())
# num=1
# while num<=n:
#     i=1
#     total=0
#     while i<num:
#         if num%i==0:
#             total+=i
#         i+=1
#     if total==num:
#         print(num,end=" ")
#     num+=1
# print()

# # Q95. Find All Pairs Whose Sum Is N
# n=int(input())
# a=1
# while a<n-a:
#     b=n-a
#     print(a,"+",b)
#     a+=1

# # Q96. Print All Two-Digit Numbers with a Given Digit Sum
# s=int(input())
# num=10
# while num<=99:
#     first=num//10
#     last=num%10
#     if first+last==s:
#         print(num,end=" ")
#     num+=1
# print()

# # Q97. Find All Common Divisors of Two Numbers
# a=int(input())
# b=int(input())
# i=1
# while i<=a and i<=b:
#     if a%i==0 and b%i==0:
#         print(i,end=" ")
#     i+=1
# print()

# # Q98. Find Prime Factor Pairs
# n=int(input("Enter a number : "))
# a=2
# found=False
# while a*a<=n:
#     if n%a==0:
#         b=n//a
#         j=2
#         prime_a=True
#         while j<a:
#             if a%j==0:
#                 prime_a=False
#                 break
#             j+=1
#         j=2
#         prime_b=True
#         while j<b:
#             if b%j==0:
#                 prime_b=False
#                 break
#             j+=1
#         if prime_a and prime_b:
#             print(a,"*",b)
#             found=True
#     a+=1
# if not found:
#     print("No prime factor pair")

# print("Thank you")