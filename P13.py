'''
Create a function taking a positive integer between 1 and 3999 (both included)
as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the leftmost
digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.
'''

def solution(n):
    n_str = str(n)
    if (len(n_str) == 1):
        return calcula_unidade(n)
    if (len(n_str) == 2):
        return calcula_decimal(n)
    if (len(n_str) == 3):
        return calcula_centena(n)
    if (len(n_str) == 4):
        return calcula_milhar(n)
    return -1
def calcula_unidade(N):
    if (N<5):
        if (N == 1):
            return "I"
        if (N == 4):
            return "IV"
        if (N == 3):
            return "III"
        if (N == 2):
            return "II"

    if (N == 5):
        return "V"
    if (N>5):
        if (N==6):
            return "VI"
        if (N==7):
            return "VII"
        if (N==8):
            return "VIII"
        if (N==9):
            return "IX"
def calcula_decimal(N):
    if (N == 10):
        return "X"
    if (N>10):
        num_x = int(str(N)[0])
        str_x = ""
        if (num_x < 4):
            for number in range(0,num_x,1):
                str_x += "X"
        if (num_x == 4):
            str_x += "XL"
        if (num_x == 5):
                str_x += "L"
        if (num_x == 6):
            str_x += "LX"
        if (num_x == 7):
            str_x += "LXX"
        if (num_x == 8):
            str_x += "LXXX"
        if (num_x == 9):
            str_x += "XC"
        if (int(str(N)[1])>0):
            str_x += calcula_unidade(int(str(N)[1]))
    return str_x
def calcula_centena(N):
    if (N == 100):
        return "C"
    if (N>100):
        num_c = int(str(N)[0])
        str_c = ""
        if (num_c<3):
            for number in range(0,num_c):
                str_c += "C"
        if (num_c == 4):
            str_c += "CD"
        if (num_c == 5):
            str_c += "D"
        if (num_c == 6):
            str_c += "DC"
        if (num_c == 7):
            str_c += "DCC"
        if (num_c == 8):
            str_c += "DCCC"
        if (num_c == 9):
            str_c += "CM"

        if (int(str(N)[1] + str(N)[2])>=10):
            str_c += calcula_decimal(int(str(N)[1] + str(N)[2]))
        elif (int(str(N)[1] + str(N)[2])== 00):
            str_c += ""
        else:
            str_c += calcula_unidade(int(str(N)[2]))
        return str_c
def calcula_milhar(N):
    if (N == 1000):
        return "M"
    num_M = int(str(N)[0])
    str_M = ""
    if (num_M<=3):
        for number in range(0,num_M):
            str_M += "M"
    if (int(str(N)[1])>0):
        str_c = int(str(N)[1] + str(N)[2] + str(N)[3])
        str_M += calcula_centena(str_c)
    elif int(str(N)[2])>0:
        str_c = int(str(N)[2] + str(N)[3])
        str_M += calcula_decimal(str_c)
    elif int(str(N)[3])>0:
        str_c = int(str(N)[3])
        str_M += calcula_unidade(str_c)
    return str_M



print(solution(1))
print(solution(4))
print(solution(6))
print(solution(14))
print(solution(21))
print(solution(89))
print(solution(91))
print(solution(984))
print(solution(1000))
print(solution(1889))
print(solution(1989))


