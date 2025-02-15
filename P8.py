'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.
'''

def persistence(n):
    n = str(n)
    mult = 1
    count = 0
    while (len(n) > 1):
        for number in range(0, len(n), 1):
            mult *= int(n[number])
        n = str(mult)
        mult = 1
        count += 1
    return count


print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))