
import random

playgame = False

while playgame == False:
    userbegin = input('Would you like to see how long it takes to roll \'Yahtzee!\'? Y/N:')
    if (userbegin.upper()) == 'Y':
        playgame = True

if playgame == True:
    print('Let\'s Begin!')
    def roll_dice():
        return [random.randint(1, 6) for i in range(5)]

    def has_yahtzee(dice):
        return len(set(dice)) == 1

    def play_game(game_num):
        for roll in range(1, 4):
            dice = roll_dice()
            print("  Roll", roll, ":", dice)
            if has_yahtzee(dice):
                return True
        return False

    def main():
        games = 0

        while True:
            games += 1
            print("Game", games)
            if play_game(games):
                break

        print("\nIt took", games, "game(s) to get a Yahtzee!")

    main()