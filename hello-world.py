from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])


if food == 'bacon' or food == 'steak':
    print("meat")
elif food == 'apple' or food == 'grape':
    print("fruit")
else: print("yuck")