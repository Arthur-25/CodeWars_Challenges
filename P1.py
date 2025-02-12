#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    str_phone_number = "("
    for number in range(0,10,1):
        str_phone_number += str(n[number])
        if (number == 2):
            str_phone_number += ") "
        if (number == 5):
            str_phone_number += "-"
    return str_phone_number

array_n1 = [1,2,3,4,5,6,7,8,9,0]
array_n2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
array_n3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
array_n4 = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]
array_n5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(create_phone_number(array_n1))
print(create_phone_number(array_n2))
print(create_phone_number(array_n3))
print(create_phone_number(array_n4))
print(create_phone_number(array_n5))
