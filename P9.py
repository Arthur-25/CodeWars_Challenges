'''
everytime you press the button it sends you an array of one-letter strings representing directions to walk
(eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction)
and you know it takes you one minute to traverse one city block, so create a function that will return true
if the walk the app gives you will take you exactly ten minutes
(you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
'''

def is_valid_walk(walk):
    if (walk.count('n') != walk.count('s') or walk.count('w') != walk.count('e')):
        return False
    if (len(walk) == 10):
        return True
    return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk(['w']))
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))
