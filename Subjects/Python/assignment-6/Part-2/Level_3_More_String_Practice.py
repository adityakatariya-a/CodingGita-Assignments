# # Level 3 — More String Practice --------=====------=======----------



# # Q86. Count Words
# s = input("Enter a sentence: ")

# words = s.split()

# print(len(words))


# # Q87. Replace All 'a' with 'e'
# s = input("Enter a string: ")

# result = s.replace('a', 'e')

# print(result)


# # Q88. Check for a Character
# s = input("Enter a string: ")
# ch = input("Enter a character: ")

# if ch in s:
#     print(True)
# else:
#     print(False)


# # Q89. Compare Two Strings
# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# if s1 == s2:
#     print(True)
# else:
#     print(False)


# # Q90. Count Digits in a String
# s = input("Enter a string: ")

# count = 0

# for ch in s:
#     if ch.isdigit():
#         count += 1

# print(count)


# # Q91. Count Uppercase Letters
# s = input("Enter a string: ")

# count = 0

# for ch in s:
#     if ch.isupper() and ch.isalpha():
#         count += 1

# print(count)


# # Q92. Count Lowercase Letters
# s = input("Enter a string: ")

# count = 0

# for ch in s:
#     if ch.islower() and ch.isalpha():
#         count += 1

# print(count)


# # Q93. Remove All Vowels
# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if ch not in "aeiouAEIOU":
#         result += ch

# print(result)


# # Q94. Remove All Digits
# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if not ch.isdigit():
#         result += ch

# print(result)


# # Q95. Toggle Character Case
# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if ch.islower():
#         result += ch.upper()
#     elif ch.isupper():
#         result += ch.lower()
#     else:
#         result += ch

# print(result)
