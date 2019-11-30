from poker.game import Game
from poker.poker import winner

if __name__ == '__main__':
    game = Game()
    single_card = game.get_single_card()
    print(single_card)
    
    player1 = game.get_a_hand()
    print(player1)

    hand1, hand2 = game.get_two_hands()
    print("Player 1: {}".format(hand1))
    print("Player 2: {}".format(hand2))

    win = winner(hand1, hand2)
    if win in [1, 2]:
        print("The winner is {}".format(win))
    else:
        print("It is a draw.")