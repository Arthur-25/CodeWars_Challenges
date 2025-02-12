#create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(l):
    l2 = l.copy()
    for number in l:
        if (type(number) == str):
            l2.remove(number)
    return l2

array_l = [1,2,'a','b']
array_l2 = [1, 'a', 'b', 0, 15]
array_l3 = [1, 2, 'aasf', '1', '123', 123]

print(filter_list(array_l))
print(filter_list(array_l2))
print(filter_list(array_l3))
