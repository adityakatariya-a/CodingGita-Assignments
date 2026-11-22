# # Level 1 — Basic Number Logic ---------==========----------



# # Q66. Count Digits
# n = int(input("Enter a number: "))

# n = abs(n)
# count = 0

# if n == 0:
#     count = 1
# else:
#     while n > 0:
#         n = n // 10
#         count = count + 1

# print(count)


# # Q67. Sum of Digits
# n = int(input("Enter a number: "))

# n = abs(n)
# total = 0

# while n > 0:
#     digit = n % 10
#     total = total + digit
#     n = n // 10

# print(total)


# # Q68. Product of Digits
# n = int(input("Enter a number: "))

# n = abs(n)
# product = 1

# if n == 0:
#     product = 0
# else:
#     while n > 0:
#         digit = n % 10
#         product = product * digit
#         n = n // 10

# print(product)


# # Q69. Reverse a Number
# n = int(input("Enter a number: "))

# sign = 1

# if n < 0:
#     sign = -1

# n = abs(n)
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# print(sign * reverse)


# # Q70. Palindrome Number
# n = int(input("Enter a number: "))

# original = n
# temp = abs(n)
# reverse = 0

# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp = temp // 10

# if n >= 0 and original == reverse:
#     print("True")
# else:
#     print("False")


# # Q71. Prime Number
# n = int(input("Enter a number: "))

# is_prime = True

# if n < 2:
#     is_prime = False
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break

# print(is_prime)


# # Q72. Primes from 1 to N
# n = int(input("Enter N: "))

# for i in range(2, n + 1):
#     is_prime = True

#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(i, end=" ")


# # Q73. First N Fibonacci Numbers
# n = int(input("Enter N: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")

#     c = a + b
#     a = b
#     b = c


# # Q74. GCD of Two Numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     remainder = a % b
#     a = b
#     b = remainder

# print(a)


# # Q75. LCM of Two Numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# x = a
# y = b

# while y != 0:
#     remainder = x % y
#     x = y
#     y = remainder

# gcd = x

# lcm = (a * b) // gcd

# print(lcm)

