name = input('Enter your name: ')
print('Welcome', name, 'to this adventure' )

answer = input('You are on a dirt road, you have come to an end and you can go left or right. which way would you like to go? ').lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim accross')

    if answer == 'swim':
        print('You swam acrross and you were eaten by a shark')
    elif answer == 'walk':
        print('You walked for many miles, ran out of food and water and you lost the game')
    else:
        print('Not a valid option. You lose.')
elif answer == 'right':
    answer = input('You came to a bridge, it looks wobbly, do you want to cross or head back?')
    if answer == 'back':
        print('You went back and were eaten by a bear')
    elif answer == 'cross':
        answer = input('you crossed the bridge and met a stranger would you talk to them? ')

        if answer == 'yes':
            print('This man saved you and you won the game')
        elif answer == 'no':
            print('He got mad and killed you')
        else:
            print('Not a valid option. You lose.')

    else:
        print('Not a valid option. You lose.')

else:
    print('not a valid option. You lose.')