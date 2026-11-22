# # Level 2 — Compare Items and Find Pairs ----=====-------======-----



# # Q101. Pairs of Digits with a Target Sum
# number = input("Enter a number: ")
# target = int(input("Enter target sum: "))

# for i in range(len(number)):
#     for j in range(i + 1, len(number)):
#         if int(number[i]) + int(number[j]) == target:
#             print(number[i], number[j])


# # Q102. Digit Pairs with a Fixed Difference
# number = input("Enter a number: ")
# D = int(input("Enter difference: "))

# for i in range(len(number)):
#     for j in range(i + 1, len(number)):
#         if abs(int(number[i]) - int(number[j])) == D:
#             print(number[i], number[j])


# # Q103. Repeated Digits in a Number
# number = input("Enter a number: ")

# for i in range(len(number)):
#     count = 0

#     for j in range(len(number)):
#         if number[i] == number[j]:
#             count += 1

#     if count > 1 and number[i] not in number[:i]:
#         print(number[i])


# # Q104. Count Equal Digit Pairs
# number = input("Enter a number: ")

# count = 0

# for i in range(len(number)):
#     for j in range(i + 1, len(number)):
#         if number[i] == number[j]:
#             count += 1

# print(count)


# # Q105. Common Characters in Two Strings
# first = input("Enter first string: ")
# second = input("Enter second string: ")

# for i in range(len(first)):
#     if first[i] in second and first[i] not in first[:i]:
#         print(first[i])


# # Q106. Check Whether Two Strings Share a Character
# first = input("Enter first string: ")
# second = input("Enter second string: ")

# found = False

# for i in range(len(first)):
#     for j in range(len(second)):
#         if first[i] == second[j]:
#             found = True
#             break

#     if found:
#         break

# print(found)


# # Q107. Seating Plan
# rows = int(input("Enter number of rows: "))
# seats_per_row = int(input("Enter seats per row: "))

# for i in range(1, rows + 1):
#     print("Row", i, ":", end=" ")

#     for j in range(1, seats_per_row + 1):
#         print(j, end=" ")

#     print()


# # Q108. Student Marks and Class Total
# S = int(input("Enter number of students: "))
# T = int(input("Enter number of tests: "))

# class_total = 0

# for i in range(1, S + 1):
#     student_total = 0

#     for j in range(1, T + 1):
#         marks = int(input("Enter marks: "))
#         student_total += marks

#     print("Student", i, "total:", student_total)

#     class_total += student_total

# print("Class total:", class_total)


# # Q109. Daily Rainfall Summary
# D = int(input("Enter number of days: "))
# S = int(input("Enter number of stations: "))

# for i in range(1, D + 1):
#     daily_total = 0

#     for j in range(1, S + 1):
#         rainfall = float(input("Enter rainfall: "))
#         daily_total += rainfall

#     print("Day", i, "total:", daily_total)


# # Q110. Largest of Several Numbers in Each Group
# G = int(input("Enter number of groups: "))
# K = int(input("Enter numbers per group: "))

# for i in range(1, G + 1):
#     largest = int(input("Enter number: "))

#     for j in range(1, K):
#         num = int(input("Enter number: "))

#         if num > largest:
#             largest = num

#     print(largest)


# # Q111. Sum of Numbers by Group and Position
# position1 = 0
# position2 = 0
# position3 = 0

# print("Enter Group 1:")

# group1_total = 0

# for j in range(1, 4):
#     num = int(input("Enter number: "))
#     group1_total += num

#     if j == 1:
#         position1 += num
#     elif j == 2:
#         position2 += num
#     else:
#         position3 += num

# print("Enter Group 2:")

# group2_total = 0

# for j in range(1, 4):
#     num = int(input("Enter number: "))
#     group2_total += num

#     if j == 1:
#         position1 += num
#     elif j == 2:
#         position2 += num
#     else:
#         position3 += num

# print("Group sums:", group1_total, group2_total)
# print("Position sums:", position1, position2, position3)


# # Q112. Number Pair Comparison Table
# N = int(input("Enter N: "))

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         print(i + j, end=" ")

#     print()


# # Q113. Count Zeroes in a Number Sequence
# N = int(input("Enter N: "))

# count = 0

# for i in range(1, N + 1):
#     num = int(input("Enter number: "))

#     if num == 0:
#         count += 1

# print(count)


# # Q114. Print Row and Column Coordinates
# R = int(input("Enter number of rows: "))
# C = int(input("Enter number of columns: "))

# for i in range(R):
#     for j in range(C):
#         print("(", i, ", ", j, ")", sep="", end=" ")

#     print()


# # Q115. Find Every Occurrence of a Substring
# text = input("Enter text: ")
# pattern = input("Enter pattern: ")

# for i in range(len(text) - len(pattern) + 1):
#     match = True

#     for j in range(len(pattern)):
#         if text[i + j] != pattern[j]:
#             match = False
#             break

#     if match:
#         print(i, end=" ")


# # Q116. Count Matching Character Pairs
# s = input("Enter a string: ")

# count = 0

# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if s[i] == s[j]:
#             count += 1

# print(count)


# # Q117. Check Whether Two Strings Are Anagrams
# first = input("Enter first string: ")
# second = input("Enter second string: ")

# is_anagram = True

# if len(first) != len(second):
#     is_anagram = False
# else:
#     for i in range(len(first)):
#         count1 = 0
#         count2 = 0

#         for j in range(len(first)):
#             if first[i] == first[j]:
#                 count1 += 1

#             if first[i] == second[j]:
#                 count2 += 1

#         if count1 != count2:
#             is_anagram = False
#             break

# print(is_anagram)


# # Q118. Print Character Frequency Without a Dictionary
# s = input("Enter a string: ")

# for i in range(len(s)):
#     if s[i] not in s[:i]:
#         count = 0

#         for j in range(len(s)):
#             if s[i] == s[j]:
#                 count += 1

#         print(s[i], ":", count)


# # Q119. Find Repeated Adjacent Characters
# s = input("Enter a string: ")

# i = 0

# while i < len(s):
#     count = 1

#     while i + count < len(s) and s[i] == s[i + count]:
#         count += 1

#     if count >= 2:
#         print(s[i], ":", count)

#     i += count


# # Q120. Compare Two Words Position by Position
# first = input("Enter first string: ")
# second = input("Enter second string: ")

# count = 0

# for i in range(len(first)):
#     if first[i] != second[i]:
#         count += 1

# print(count)