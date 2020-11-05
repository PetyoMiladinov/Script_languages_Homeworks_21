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

s_list = [1, 58, 129, 59, 219, 10098, 2, 8237, 2189]

max_num = max(s_list)
min_num = min(s_list)
answer = max_num - min_num

print ("Answer is: ", answer)

##Задача 3: 

string = input ("Enter a string: ")

digits = letters = 0

for c in string:
    if c.isdigit():
        digits = digits + 1
    elif c.isalpha():
        letters = letters + 1
    else:
        pass
        
print("Bukvi: ", letters)
print("Tsifri: ", digits)