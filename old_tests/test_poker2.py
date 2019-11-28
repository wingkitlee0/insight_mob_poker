


# def test_poker():
#     assert True

# def test_highest_card():
#     assert find_highest_card("2H 3D 5S 9C KD") == "KD"

# def test_highest_card2():
#     assert find_highest_card("2C 3H 4S 8C AH") == "AH"

# def test_highest_card3():
#     assert find_highest_card("2C 3H 4S AD AH") in {"AD", "AH"}

# def test_get_rank_from_card_1():
#     assert get_rank_from_card("2H") == 2

# def test_get_rank_from_card_2():
#     assert get_rank_from_card("10H") == 10

# def test_winner():
#     assert winner("2C 3H 4S AD AH", "2C 3H 4S KD KH") == 1

# def test_winner1():
#     assert winner("2C 3H 4S 2D AH", "2C 3H 4S AD KH") == 2

# def test_winner2():
#     assert winner("2C 3H 4S 2D AH", "2C 3H 4S 2D AH") == 0

# def test_winner3():
#     assert winner("2C 3H 4S AD AH", "2C 3H 4S AD KH") == 1

def test_card_1():
    card = Card("AH")
    assert card.str_card == "AH"

def test_card_2():
    card = Card("AH")
    assert card.rank == 14

def test_compare_cards():
    card1 = Card("AH")
    card2 = Card("KD")
    assert card1.rank > card2.rank

def test_compare_cards2():
    card1 = Card("AH")
    card2 = Card("AD")
    assert card1.rank == card2.rank

def test_compare_cards3():
    card1 = Card("3H")
    card2 = Card("AC")
    assert card1.rank < card2.rank

def test_suit():
    card = Card("7C")
    assert card.suit == "C"

#def test_hand():
#    hand = Hand("2C 3H 4S JD KH")
#    assert hand.highest_card.str_card == "KH"

class Hand:
    def __init__(self, str_hand):
        self.str_hand = str_hand
        self.card_list = []
        for card in str_hand.split(" "):
            self.card_list.append(Card(card))


class Card:
    def __init__(self, str_card):
        self.str_card = str_card
        
        self.card_dict = {'A':14, 'K':13 , 'Q':12, 'J':11}
        for i in range(2,11,1):
            self.card_dict[str(i)] = i
        self.rank = self.get_rank_from_card()
        self.suit = self.str_card[-1]

    def get_rank_from_card(self):
        # "2H" -> 2
        return self.card_dict[self.str_card[:-1]]


def get_rank_from_card(card):
    # "2H" -> 2
    card_dict = {'A':14, 'K':13 , 'Q':12, 'J':11}
    for i in range(2,11,1):
        card_dict[str(i)] = i 
    return card_dict[card[:-1]]

def find_highest_card(cards_list):
    # cards: string
    highest_card = cards_list[0]
    highest_card_rank = get_rank_from_card(cards_list[0])
    for card in cards_list[1:]:
        if get_rank_from_card(card) > highest_card_rank:
            highest_card = card
            highest_card_rank = get_rank_from_card(highest_card)
    
    # card_list = card_list.remove(highest_card)
    # card_list = " ".join([x for x in card_list])
    return highest_card


def winner(hand1, hand2):
    """1 hand1 wins, 0 draw, 2 hand2 wins"""
    highest_card_hand1 = find_highest_card(hand1.split(" "))
    highest_card_hand2 = find_highest_card(hand2.split(" "))

    if get_rank_from_card(highest_card_hand1) > get_rank_from_card(highest_card_hand2): 
        return 1  # Return 1
    if get_rank_from_card(highest_card_hand1) < get_rank_from_card(highest_card_hand2): 
        return 2  # Return 2
    return 0




    
