import random

def roll_dice(): 
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def main():
    player1 = input("Enter Player 1 name:\n")
    player2 = input("Enter Player 2 name:\n")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1 > roll2:
        print(player1, 'wins!')
    elif roll2 > roll1:
        print(player2, 'wins!')
    else:
        print('You tie!')

main()

#prints the following
#Enter Player 1 name:
#cat <--user entered
#Enter Player 2 name:
#mouse <--user entered
#cat rolled 7
#mouse rolled 6
#cat wins!
