# # Level 5 — Advanced Shapes and Challenges



# # Q43. Butterfly Pattern
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")

#     for j in range(2 * (n - i)):
#         print(" ", end="")

#     for j in range(i):
#         print("*", end="")

#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print("*", end="")

#     for j in range(2 * (n - i)):
#         print(" ", end="")

#     for j in range(i):
#         print("*", end="")

#     print()


# # Q44. Hollow Hourglass
# n = int(input("Enter size: "))

# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         if i == n or j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()

# for i in range(2, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()


# # Q45. Alphabet Diamond
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(1, i + 1):
#         print(chr(64 + j), end="")

#     for j in range(i - 1, 0, -1):
#         print(chr(64 + j), end="")

#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(1, i + 1):
#         print(chr(64 + j), end="")

#     for j in range(i - 1, 0, -1):
#         print(chr(64 + j), end="")

#     print()


# # Q46. Pascal's Triangle
# n = int(input("Enter size: "))

# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")

#     num = 1

#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)

#     print()


# # Q47. Heart Pattern
# n = int(input("Enter size: "))

# for i in range(1, n // 2 + 1):
#     for j in range(n // 2 - i):
#         print(" ", end="")

#     for j in range(2 * i):
#         print("*", end="")

#     for j in range(2 * (n // 2 - i) + 1):
#         print(" ", end="")

#     for j in range(2 * i):
#         print("*", end="")

#     print()

# for j in range(2 * n - 1):
#     print("*", end="")
# print()

# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()


# # Q48. Hollow Heart
# n = int(input("Enter size: "))
# width = 2 * n - 1

# for i in range(n - 1):
#     for j in range(width):
#         if i == 0:
#             if j == 1 or j == 2 or j == width - 3 or j == width - 2:
#                 print("*", end="")
#             else:
#                 print(" ", end="")

#         elif i == 1:
#             if j == 0 or j == 3 or j == width - 4 or j == width - 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")

#         else:
#             if j == 0 or j == n - 1 or j == width - 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")

#     print()

# for i in range(1, n):
#     for j in range(width):
#         if j == i or j == width - 1 - i:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()


# # Q49. Star-and-Space Center Pattern
# n = int(input("Enter odd size: "))

# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1 or i == n // 2:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()


# # Q50. Custom Symbol Square
# n = int(input("Enter size: "))
# symbol = input("Enter symbol: ")

# for i in range(n):
#     for j in range(n):
#         print(symbol, end="")
#     print()


# # Q51. User-Sized Hollow Rectangle
# rows = int(input("Enter rows: "))
# columns = int(input("Enter columns: "))

# for i in range(rows):
#     for j in range(columns):
#         if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()


# # Q52. Create Your Own Pattern
# n = int(input("Enter size: "))
# symbol = input("Enter symbol: ")

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         print(symbol, end="")

#     print()