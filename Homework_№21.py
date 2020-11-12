##Задача 1:
print("1.")
num = int(input("Enter a number: "))
count = int(input("Enter a second number: "))

print(f"{num}, {count} -->", end='')

for i in range(1, count+1):
    print(i * num, end=' ')
print("")

##Задача 2:
print("2.")
string = input("Say something: ")
vowel = 0
#vowel_option = ["a", "e", "i", "o", "u"]

for i in range(0):
    if "a" or "A" or "e" or "E" or "i" or "I" or "o" or "O" or "u" or "U" in string:
        vowel = vowel + 1

print(string + "-->", end=' ')
print(vowel)

##Задача 3:
print("3.")
given_list = ["my", 1, "turtle", "explain", 3.14, "1", "3.14"]
result = []

for el in given_list:
    if not isinstance(el, (int, float)):
        result.append(el)

print(f"result: {result}")

##Задача 4:
print("4.")
number = input("Enter a number: ")
is_palindrom = number == number[::-1]
print(f"Number {number} --> {is_palindrom}")

##Задача 5:
print("Bonus.")
print("Не можах да го измисля.")

#Предният път:
##########################################################################################
##Задача 1:
# num = 2000;
# comma = '\b,';

# while num <= 5000: 
    # print (num, comma)
    # #print (",")
    # num += 2;

# num = 2000;
# comma = '\b,';
# bol = True;

# if "1" in str(num) or "3" in str(num) or "5" in str(num) or "7" in str(num) or "9" in str(num):
        # bol = False;

# while num <= 5000 and bol == True:
    # print (num, comma)
    # num += 2;

# digit = [1, 3, 5, 7, 9]


# for digit in num:
    # bol = False
    # else: 
        # if: 
            # bol = True
            # print (num, comma)

##Задача 2: 

# s_list = [1, 58, 129, 59, 219, 10098, 2, 8237, 2189]

# max_num = max(s_list)
# min_num = min(s_list)
# answer = max_num - min_num

# print ("Answer is: ", answer)

##Задача 3: 

# string = input ("Enter a string: ")

# digits = letters = 0

# for c in string:
    # if c.isdigit():
        # digits = digits + 1
    # elif c.isalpha():
        # letters = letters + 1
    # else:
        # pass
        
# print("Bukvi: ", letters)
# print("Tsifri: ", digits)