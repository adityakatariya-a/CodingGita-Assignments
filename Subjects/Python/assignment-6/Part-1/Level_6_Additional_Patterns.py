# # Level 6 — Additional Patterns --------========-------




# # Q53	Decreasing outer loop
# n = int(input("Enter size: "))

# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# # Q54	Fixed rows and columns
# n = int(input("Enter size: "))

# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()


# # Q55	Spaces + odd number of stars
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()


# # Q56	Reverse loop
# n = int(input("Enter size: "))

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()


# # Q57	Increasing nested loops
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()


# # Q58	Increasing spaces + decreasing stars
# n = int(input("Enter size: "))

# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(i):
#         print("*", end="")

#     print()


# # Q59	Right alignment
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(i):
#         print("*", end="")

#     print()


# # Q60	Increasing spaces + decreasing number range
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(i - 1):
#         print(" ", end="")

#     for j in range(i, n + 1):
#         print(j, end=" ")

#     print()


# # Q61	Hollow pattern conditions
# n = int(input("Enter size: "))

# for i in range(n):
#     for j in range(n - i):
#         if i == 0 or j == 0 or j == n - i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()


# # Q62	Upper and lower hollow pyramids
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()


# # Q63	Diagonal conditions
# n = int(input("Enter size: "))

# for i in range(n):
#     for j in range(n):
#         if j == i or j == n - i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(n - 2, -1, -1):
#     for j in range(n):
#         if j == i or j == n - i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# # Q64	Increasing and decreasing triangles
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()


# # Q65	Testing different input sizes
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()