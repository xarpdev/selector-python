"""
Selector Python Project, a random selector to tell me who I have to visit today using import ramdom by Santiago Fabián Quispe.
"""

import random

friends = [
    'Dino',
    'Yamil',
    'Carla',
    'Armando',
    'Rosa',
    'Tomás',
    'María'
]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(friends) # randomly choose a friend

print('Who will I spend the day with today?')
print(selected)