# Задача 1:

print("1. ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
def is_equal(a, b, c):
    # a = int(input("Enter a: "))
    # b = int(input("Enter b: "))
    # c = int(input("Enter c: "))
    # is_equal()

    last_digit_a = a % 10
    last_digit_b = b % 10
    last_digit_c = c % 10
    l_ab = last_digit_a * last_digit_b

    if l_ab == last_digit_c:
        print("True")
    else:
        print("False")

# Задача 2:
print("2. ")
limit = int(input("Enter speed limit: "))
distance = int(input("Enter the distance: "))
def speeding(limit, distance):
    time = distance / limit
    end_limit = limit + 15
    second_time = distance / end_limit
    end_time = time - second_time

    # Резултат:
    print("speeding", end=" ")
    return(end_time)*60



is_equal()
speeding()

# limit = int(input("Enter speed limit: "))
# distance = int(input("Enter the distance: "))
# time = distance/limit
# end_limit = limit + 15
# end_time = distance/end_limit
#
# # Резултат:
# print(time - end_time)
