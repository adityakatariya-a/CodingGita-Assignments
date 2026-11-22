# # Level 2 — Spaces and Alignment


# # Q13. Right-Aligned Half Pyramid
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(i):
#         print("*", end="")

#     print()


# # Q14. Inverted Right-Aligned Half Pyramid
# n = int(input("Enter size: "))

# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(i):
#         print("*", end="")

#     print()


# # Q15. Star Pyramid
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()


# # Q16. Inverted Star Pyramid
# n = int(input("Enter size: "))

# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()


# # Q17. Solid Diamond
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()


# # Q18. Rhombus
# n = int(input("Enter size: "))

# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")

#     for j in range(n):
#         print("*", end="")

#     print()


# # Q19. Mirrored Number Pattern
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")

#     for j in range(2 * (n - i)):
#         print(" ", end="")

#     for j in range(i, 0, -1):
#         print(j, end="")

#     print()


# # Q20. Centered Number Pyramid
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(1, i + 1):
#         print(j, end=" ")

#     print()


# # Q21. Palindromic Number Pyramid
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(1, i + 1):
#         print(j, end="")

#     for j in range(i - 1, 0, -1):
#         print(j, end="")

#     print()


# # Q22. Alphabet Palindrome Pyramid
# n = int(input("Enter size: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(i):
#         print(chr(64 + j + 1), end="")

#     for j in range(i - 1, 0, -1):
#         print(chr(64 + j), end="")

#     print()


# # Q23. Reverse-Starting Alphabet Triangle
# n = int(input("Enter size: "))

# for i in range(n, 0, -1):
#     for j in range(i, n + 1):
#         print(chr(64 + j), end=" ")

#     print()