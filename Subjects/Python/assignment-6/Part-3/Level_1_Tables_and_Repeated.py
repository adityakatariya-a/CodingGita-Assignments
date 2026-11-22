# # Level 1 — Tables and Repeated Calculations



# # Q96. Multiplication Tables from 1 to N
# N = int(input("Enter N: "))
# K = int(input("Enter K: "))

# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         print(i, "x", j, "=", i * j)


# # Q97. Number and Its Divisors
# N = int(input("Enter N: "))

# for i in range(1, N + 1):
#     print(i, end=": ")

#     for j in range(1, i + 1):
#         if i % j == 0:
#             print(j, end=" ")

#     print()


# # Q98. Count Divisors for Every Number
# N = int(input("Enter N: "))

# for i in range(1, N + 1):
#     count = 0

#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1

#     print(i, ":", count)


# # Q99. Perfect Numbers in a Range
# N = int(input("Enter N: "))

# for i in range(1, N + 1):
#     total = 0

#     for j in range(1, i):
#         if i % j == 0:
#             total += j

#     if total == i:
#         print(i)


# # Q100. Prime Numbers in a Range
# N = int(input("Enter N: "))

# for i in range(2, N + 1):
#     is_prime = True

#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(i, end=" ")
