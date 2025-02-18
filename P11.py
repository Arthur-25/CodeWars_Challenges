'''
Given two integers a and b, which can be positive or negative,
find the sum of all the integers between and including them and return it.
If the two numbers are equal return a or b.

Note: a and b are not ordered!
'''

def find_smaller(n1,n2):
    if (n1<n2):
        return n1
    if (n2<n1):
        return n2
    if (n1 == n2):
        return n1
def find_bigger(n1,n2):
    if (n1>n2):
        return n1
    if (n2>n1):
        return n2
    if (n1 == n2):
        return n1
def get_sum(a,b):
    if a == b:
        return a

    start = min(a, b)
    end = max(a, b)
    sum = 0

    for i in range(start, end + 1):
        sum += i

    return sum
print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))
