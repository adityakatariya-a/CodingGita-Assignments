# # Level 3 — Challenge Problems --------=========-------=========---------



# # Q121. Print All Pythagorean Triples up to N
# N = int(input("Enter N: "))

# for a in range(1, N + 1):
#     for b in range(a + 1, N + 1):
#         for c in range(b + 1, N + 1):
#             if a * a + b * b == c * c:
#                 print(a, b, c)


# # Q122. Find Numbers Equal to the Sum of Their Proper Divisors
# N = int(input("Enter N: "))

# for i in range(2, N + 1):
#     total = 0

#     for j in range(1, i):
#         if i % j == 0:
#             total += j

#     if total == i:
#         print(i)


# # Q123. Print Unique Products in Increasing Factor Order
# N = int(input("Enter N: "))

# for i in range(1, N + 1):
#     for j in range(i, N + 1):
#         product = i * j
#         found = False

#         for p in range(1, N + 1):
#             for q in range(p, N + 1):

#                 if p < i or (p == i and q < j):
#                     if p * q == product:
#                         found = True

#         if not found:
#             print(product, end=" ")


# # Q124. Find All Pairs of Prime Numbers with a Given Sum
# N = int(input("Enter an even number: "))

# for i in range(2, N // 2 + 1):
#     j = N - i

#     prime1 = True
#     prime2 = True

#     for k in range(2, i):
#         if i % k == 0:
#             prime1 = False
#             break

#     for k in range(2, j):
#         if j % k == 0:
#             prime2 = False
#             break

#     if prime1 and prime2:
#         print(i, j)


# # Q125. Check a Magic-Sum Pattern
# N = int(input("Enter an odd number: "))

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         print(i + j, end=" ")

#     print()

# print("Row sums:", end=" ")

# for i in range(1, N + 1):
#     total = 0

#     for j in range(1, N + 1):
#         total += i + j

#     print(total, end=" ")


# # Q126. Count Peaks in a Number Sequence
# N = int(input("Enter N: "))

# count = 0

# if N >= 3:
#     previous = int(input("Enter number: "))
#     current = int(input("Enter number: "))

#     for i in range(3, N + 1):
#         next_num = int(input("Enter number: "))

#         if current > previous and current > next_num:
#             count += 1

#         previous = current
#         current = next_num

# print(count)


# # Q127. Find Repeated Digit Sums

# number = input("Enter a number: ")

# found = False

# for i in range(len(number)):
#     for j in range(i + 1, len(number)):

#         sum1 = int(number[i]) + int(number[j])

#         for k in range(len(number)):
#             for l in range(k + 1, len(number)):

#                 if k > i or (k == i and l > j):
#                     sum2 = int(number[k]) + int(number[l])

#                     if sum1 == sum2:
#                         found = True
#                         break

#             if found:
#                 break

#         if found:
#             break

#     if found:
#         break

# if found:
#     print("Repeated pair sums exist")
# else:
#     print("No repeated pair sums")

# # Q128. Number Pattern from Row and Column
# N = int(input("Enter N: "))

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         print(abs(i - j), end=" ")

#     print()


# # Q129. Compare Digits with Their Neighbours
# number = input("Enter a number: ")

# count = 0

# for i in range(1, len(number) - 1):
#     if number[i] > number[i - 1] and number[i] > number[i + 1]:
#         count += 1

# print(count)


# # Q130. Count Increasing Digit Pairs
# number = input("Enter a number: ")

# count = 0

# for i in range(len(number)):
#     for j in range(i + 1, len(number)):
#         if number[i] < number[j]:
#             count += 1

# print(count)


# # Q131. Character Frequency Compression Without a Dictionary
# s = input("Enter a string: ")

# for i in range(len(s)):
#     if s[i] not in s[:i]:
#         count = 0

#         for j in range(len(s)):
#             if s[i] == s[j]:
#                 count += 1

#         print(s[i] + str(count), end="")


