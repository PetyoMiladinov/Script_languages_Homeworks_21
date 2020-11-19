import time

# Задача 1:
print("1. ")
string = input("Enter something: ")
vowels = 'aoueiAOUEI'

for vowel in vowels:
    string = string.replace(vowel, vowel * 4)

print(string)

# Задача 2:
print("2. ")
num = input("Enter a number: ")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
count = 0
print(f"{num} -->", end=" ")
time.sleep(5.5)

for i in num:
    count = count + 1

print(count)

# Задача 3:
print("3. ")
number = int(input("Enter a number: "))
number2 = number

count = 0

while number2 >= 2:
    number2 **= 0.5
    count += 1

print(f"{number} -> {count}")

# Задача 4:
print("4. ")
number3 = int(input("Enter a number: "))
add = 0

for n in range(2, number3 + 1):
    prime = True
    for m in range(2, n):
        if n % m == 0:
            prime = False
            break
    if prime:
        add += n

print(f"{number3} -> {add}")

# Коментирани части (неуспешни опити):
# string = input("Enter a string: ")
# vowels = ["a", "e", "u", "o", "i"]
# print(f"{string} -->", end=" ")
# for i in range(0):
#     if vowels in string:
#         k = vowels
#
# print(string)

#
# num_2 = int(input("Enter a number: "))
# add = 0
# print(f"{num_2} -->", end=" ")
# for n in range(1, num_2):
#     prime = True
#     for m in range(2, n + 1):
#         if n % m == 0:
#             prime = False
#     if prime:
#         add += n
#
# print(add)
