import random

fortune = random.randint(1,3)

if fortune == 1:
    print("Today will be lucky day")
elif fortune == 2:
    print("You will meet someone new and intresting")
elif fortune == 3:
    print("Watch out for obstacles in your path")

print(fortune)