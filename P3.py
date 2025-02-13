'''
The Western Suburbs Croquet Club has two categories of membership,
Senior and Open. They would like your help with an application form that will tell
prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
In this croquet club, handicaps range from -2 to +26;
the better the player the lower the handicap.
'''

def open_or_senior(data):
    list2 = []
    for number in range(0, len(data), 1):
        if (data[number][0] >= 55 and data[number][1] > 7):
            list2.append('Senior')
        else:
            list2.append('Open')
    return list2


list = [18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]
list_2 = [(16, 23),(73,1),(56, 20),(1, -1)]

print(open_or_senior(list))
print(open_or_senior(list_2))

