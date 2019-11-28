def test_poker():
    assert True

def test_highest_card():
    assert find_highest_card("2H 3D 5S 9C KD") == "KD"

def test_highest_card2():
    assert find_highest_card("2C 3H 4S 8C AH") == "AH"

def test_highest_card3():
    assert find_highest_card("2C 3H 4S AD AH") in {"AD", "AH"}

def test_get_rank_from_card_1():
    assert get_rank_from_card("2H") == 2

def test_get_rank_from_card_2():
    assert get_rank_from_card("10H") == 10

def test_winner():
    assert winner("2C 3H 4S AD AH", "2C 3H 4S KD KH") == 1

#def test_winner1():
#    assert winner("2C 3H 4S 2D AH", "2C 3H 4S AD KH") == 2

def test_winner2():
    assert winner("2C 3H 4S 2D AH", "2C 3H 4S 2D AH") == 0

#def test_winner3():
#    assert winner("2C 3H 4S AD AH", "2C 3H 4S AD KH") == 1

def get_rank_from_card(card):
    # "2H" -> 2cards.split(" ")
    card_dict = {'A':14, 'K':13 , 'Q':12, 'J':11}
    for i in range(2,11,1):
        card_dict[str(i)] = i 
    return card_dict[card[:-1]]

# function input: cards -> hand

def find_highest_card(cards):
    # cards: string
    cards_list = cards.split(" ")
    highest_card = cards_list[0]
    highest_card_rank = get_rank_from_card(cards_list[0])
    for card in cards_list[1:]:
        if get_rank_from_card(card) > highest_card_rank:
            highest_card = card
            highest_card_rank = get_rank_from_card(highest_card)
    
    return highest_card



def winner(hand1, hand2):
    """1 hand1 wins, 0 draw, 2 hand2 wins"""
    highest_card_hand1 = find_highest_card(hand1)
    highest_card_hand2 = find_highest_card(hand2)

    if get_rank_from_card(highest_card_hand1) > get_rank_from_card(highest_card_hand2): 
        return 1  # Return 1
    if get_rank_from_card(highest_card_hand1) < get_rank_from_card(highest_card_hand2): 
        return 2  # Return 2
    return 0




    
