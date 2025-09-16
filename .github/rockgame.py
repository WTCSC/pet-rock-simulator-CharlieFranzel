import random

day = 0
happiness = 100
food = 100
water = 100
alive = True

while alive == True:
    day += 1
    food -= random.randint(1, 15)
    water -= random.randint(1, 15)
    happiness -= random.randint(1, 15)
    if happiness <= 0 or food <= 0 or water <= 0:
        alive = False
    print(f'Day {day}. Food:{food}, Water:{water}, Hapiness:{happiness}')
    # START OF NEXT DAY
    print('Do nothing [0] | Feed rock [1] | Water rock [2] | Play with rock [3] | Quit [4]')
    userchoice = input('> ')
    if userchoice == '0':
        print('You neglect your rock.')
    if userchoice == '1':
        food += random.randint(9, 13)
        print('Om nom nom nom.')
        happiness += random.randint(0, 4)
    if userchoice == '2':
        water += random.randint(9, 13)
        happiness += random.randint(0, 4)
        print('Thats a thirsty rock.')
    if userchoice == '3':
        happiness += random.randint(7,10)
        water -= random.randint(2,5)
        print(f'You play fetch with your rock.')
print(f'Your rock died :( | Rock lived {day} days. )')