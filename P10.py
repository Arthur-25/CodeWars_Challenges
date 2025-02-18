
def find_nb(m):
    sum = 0
    for n in range(1, m, 1):

        count = 0
        sum = 0
        while ((n - count) ** 3 != 1 and count < m):

            count += 1
            sum += (n - count) ** 3



        if (sum == m):
            return n -1
            break
    return -1

print(find_nb(4))
print(find_nb(16))
print(find_nb(4183059834009))
