def dig_pow(n, p):
    num = str(n)
    sum = 0

    for numbers in range(0, len(num), 1):
        sum += pow(int(num[numbers]), p + numbers)
    k = 0
    while (n * k <= sum):
        if (n * k == sum):
            return k
        k += 1
    return -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
print(dig_pow(41, 5))
print(dig_pow(114, 3))
print(dig_pow(8, 3))