import random

lst=['rock','paper','scissor']
uch=input('enter rock/paper or scissor :')
computeruch=random.choice(lst)
print(f'you chose {uch}')
print(f"computer chose {computeruch}")
if uch==computeruch:
    print('its a tie')
elif (
    (uch=="rock" and computeruch=="scissor") or
    (uch=='paper' and computeruch=="rock") or
    (uch=="scissor" and computeruch=="paper")):
    print("you win")
else:
    print("computer wins")