#Game
import time
print('Welcome to the new age!')
Rknights=0
Rknights==0
print('***********************')
print('\nYou have entered the lost kingdom!')
time.sleep(2)
print('\nYour mission it to locate the missing knight \nand make it safely through the hidden gate.')

print('\nYou may choose one item to take on your journey.')
print('sword(s), lantern(l), net(n), fish(f)')
item=input('What do you choose?: ')
while not (item=='s' or item=='S' or item=='l' or item=='L' or item=='n' or item=='N' or item=='f' or item=='F'):
    item=input('That is a invalid inputer. Enter: s, l, n or f:')

choice1=input("\nYou've safely crossed the dessert do you follow the hidden path \nor the cobble stone road? Enter path or road: ")
while not (choice1=='path' or choice1=='Path' or choice1=='road' or choice1=='Road'):
    choice1=input('That is a invalid inputer. Enter: path or road:')
if choice1.lower()=='path':
    print('\nThe bushes starts to ruffle!')
    choice1a=input('Do you take a closer look or do you keep walking? \nEnter y or n:')
    while not (choice1a=='y' or choice1a=='Y' or choice1a=='n' or choice1a=='N'):
        choice1a=input('That is a invalid inputer. Enter: y or n:')
    if choice1a.lower()=='y':
        time.sleep(2)
        print('You have found a missing knight')
        if item.lower()=='f':
            print('The knight was starving and you shared your fish with them.\nAfter the knight is fed you help them back onto the cobble stone path.')
            Rknights=Rknights+1
            print('After three 3 days on the cobble stone path you made it to the hidden gate! \nKnight recovered', Rknights,'\nYou have won the game!')
        else:
                print('If you have selected the fish you would have safed the starving knight!\n')
                print('The knight starves before you make it back to the cobble stone road.\nYou lose the game!')
    else:
        print('You ignore the ruffling bushes and run back to the cobble stone path')
        print('The path through the cobble stone was smooth. You made it to the hidden gate!')
        print('Unfortounately you never found the missing knight. Knights safed:', Rknights, '\nYou failed the mission and lose the game!')
else:
    print('\nThe path is smooth and you safely made it to the diverged roads.')
    direction=input('Which terrain do you traverse? mountain, forest, or cave:')
    while not(direction=='mountain' or direction=='Mountain' or direction=='forest' or direction=='Forest'
               or direction=='cave' or direction=='Cave'):
        direction=input('That is a invalid inputer. EnterL mountain, forest or cave:')
    if direction.lower() == 'mountain':
        print('\nYou start to climb the mountain and on your way you discover an injured knight.')
        print('Both you and the night continue climbing the mountain')
        print('The injured knight slips and falls!' )
        time.sleep(2)
        if item.lower() == 'n':
            print('You throw the net and catch the falling knight! You use it to pull the knight up and continue on with your journey.')
            Rknights=Rknights+1
            print('You made it to the hidden gate! Knight recovered:', Rknights,'\nYou win the game!')
        else:
                print('If you had a net you could have safed the knight from an impending fall.')
                print('You failed the missing knight and lose the game!')

    elif direction.lower()=='forest':
        print('\nYou enter the forest and you hear a scream.')
        time.sleep(2)
        print('You approach the scream and witness a knight running away from two bandits.')
        time.sleep(2)
        if item.lower()=='s':
            print('You slay the bandits and safe the knight!')
            Rknights=Rknights+1
            print('You continue on with your journey and make it to the hidden gate! Knight recovered:',Rknights,'\nYou have won the game!')
        else:
            print('If you had a sword you could have safed the knight.')
            print('Instead the bandints slay the knight and run off with his gold.')
            print('You lose the game!')
    elif direction.lower()=='cave':
        print('\nYou enter the cave and proceed through the tunnels')
        if item.lower()=='l':
            print('You use the lantern to light the way through the tunnels.')
            time.sleep(2)
            print('During your exploration you discover the missing knight! \nYou help guide them through the rest of the tunnels.')
            Rknights=Rknights+1
            time.sleep(2)
            print('You made it to the hidden gate! Knight recovered:', Rknights, '\nYou win the game!')
        else:
                print('It gets really dark in the tunnels and you lose your way.')
                print('You never find the missing knight and instead become another missing knight.')
                print('If you had selected the lantern you could have lit your way through the tunnels.')
                print('You lose the game!')

