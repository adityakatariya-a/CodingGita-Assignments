# # Level 2 — Basic String Logic



# # Q76. Length of a String
# s = input("Enter a string: ")
# print(len(s))


# # Q77. Print Each Character
# s = input("Enter a string: ")

# for ch in s:
#     print(ch)


# # Q78. Count Vowels
# s = input("Enter a string: ")

# count = 0

# for ch in s:
#     if ch in "aeiouAEIOU":
#         count += 1

# print(count)


# # Q79. Count Consonants
# s = input("Enter a string: ")

# count = 0

# for ch in s:
#     if ch.isalpha() and ch not in "aeiouAEIOU":
#         count += 1

# print(count)


# # Q80. Convert to Uppercase
# s = input("Enter a string: ")

# print(s.upper())


# # Q81. Convert to Lowercase
# s = input("Enter a string: ")

# print(s.lower())


# # Q82. Reverse a String
# s = input("Enter a string: ")

# reverse = ""

# for i in range(len(s) - 1, -1, -1):
#     reverse += s[i]

# print(reverse)


# # Q83. Palindrome String
# s = input("Enter a string: ")

# reverse = ""

# for i in range(len(s) - 1, -1, -1):
#     reverse += s[i]

# if s == reverse:
#     print(True)
# else:
#     print(False)


# # Q84. Count a Specific Character
# s = input("Enter a string: ")

# count = 0

# for ch in s:
#     if ch == 'a' or ch == 'A':
#         count += 1

# print(count)


# # Q85. Remove All Spaces
# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if ch != " ":
#         result += ch

# print(result)