# Snake water gun game in python 
'''
Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.
In situations where both players choose the same object, the result will be a draw.

'''

import random

def swg(comp, mine):
    if (comp==mine):
        return None
    if(comp=='Snake' and mine =='Gun'):
        return True 
    elif(comp=='Water' and mine =='Snake'):
        return True 
    elif(comp=='Gun' and mine =='Water'):
        return True 
    else:
        return False

choice = ('Snake', 'Water', 'Gun')
comp = random.randint(0, 2)
comp = choice[comp]
mine = input('Choose either Snake, Water or Gun: ')

win = swg(comp, mine)
print(f"You chose {mine} and the computer chose {comp}")
if win is None:
    print("Match Drawn")
if win:
    print("You won")
else:
    print("You lose")
