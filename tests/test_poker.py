
# def test_poker():
#     assert True

from poker.poker import Card, Hand, winner

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

def test_hand_sorting():
    hand = Hand("2C 3H 4S KH JD")
    assert hand.card_list[0].str_card == "KH"

def test_hand():
    hand = Hand("2C 3H 4S JD KH")
    assert hand.highest_card.str_card == "KH"

def test_sorted_ranks():
    hand = Hand("2C 3H 4S JD KH")
    assert hand.rank_list == [13,11,4,3,2]

def test_hand_pair():
    hand = Hand("2C 3H 4S JD JH")
    assert hand.hand_type == 1

def test_hand_type_highest_card_1():
    hand = Hand("2C 3H 4S JD KH")
    assert hand.hand_type == 0

def test_hand_pair_3():
    hand = Hand("2C 3H JS JD JH")
    assert hand.hand_type != 1 # triple?

def test_hand_pair_4():
    hand = Hand("2C 3H 4S 2D AH")
    assert hand.rank_list == [2,2,14,4,3]

def test_hand_pair_5():
    hand = Hand("2C 3H 3S 2D AH")
    assert hand.rank_list == [3,3,2,2,14]

def test_hand_type_three_1():
    hand = Hand("3C 3H 3S 2D AH")
    assert hand.hand_type == 3

def test_hand_type_two_pair_1():
    hand = Hand("3C 3H 4S 4D AH")
    assert hand.hand_type == 2
    
def test_hand_type_full_house_1():
    hand = Hand("3C 3H 3S 2D 2H")
    assert hand.hand_type == 6

def test_hand_type_four_of_a_kind_1():
    hand = Hand("3C 3H 3S 3D 2H")
    assert hand.hand_type == 7

def test_hand_type_straight_1():
    hand = Hand("3C 4H 5S 6D 7H")
    assert hand.hand_type == 4

def test_hand_type_flush_1():
    hand = Hand("3C 5C 8C 9C AC")
    assert hand.hand_type == 5

def test_hand_type_straight_flush_1():
    hand = Hand("3H 4H 5H 6H 7H")
    assert hand.hand_type == 8

def test_hand_type_royal_flush_1():
    hand = Hand("10H JH QH KH AH")
    assert hand.hand_type == 9

def test_hand_same_suit():
    hand = Hand("3H 4H 5H 6H 7H")
    assert hand.same_suit == True

def test_hand_same_suit_2():
    hand = Hand("3H 4H 5H 6H 7D")
    assert hand.same_suit == False

def test_winner():
    assert winner("2C 3H 4S AD AH", "2C 3H 4S KD KH") == 1

def test_winner_1():
    # a pair in hand1
    assert winner("2C 3H 4S 2D AH", "2C 3H 4S AD KH") == 1

def test_winner_2():
    assert winner("2C 3H 4S 2D AH", "2C 3H 4S 2D AH") == 0

def test_winner_3():
    assert winner("2C 3H 4S AD AH", "2C 3H 4S AD KH") == 1

def test_winner_4():
   assert winner("2C 3H 4S 2D AH", "2C 3H 4S AD KH") == 1

def test_winner_5():
   assert winner("2C 2H 4S AD JH", "3C 3H 4S QD KH") == 2

def test_winner_6():
    assert winner("2C 2H 4S AD JH", "3C 3H 4S QD KH") == 2

def test_winner_7():
    assert winner("AD 2H 5S 9C 3D", "2C 3H 4S 8C AH") == 1

def test_winner_flush_1():
    assert winner("2C 3C 4C AC JC", "3S 6S 4S QS KS") == 1

def test_winner_flush_2():
    assert winner("2C 3C 4C 5C 6C", "2S 3S 4S 5S 6S") == 0

def test_winner_flush_3():
    assert winner("10C JC KC QC AC", "AS QS KS 10S JS") == 0

def test_winner_pair_1():
    assert winner("10C 10S KC QC AC", "AS AH KS 10S JS") == 2

def test_winner_full_house_1():
    assert winner("10C 10S 10H QC QS", "AS AH AC 9S 9H") == 2

def test_winner_four_of_a_kind_1():
    assert winner("10C 10S 10H 10D AC", "5S 5H 5D 5C JS") == 1

def test_winner_two_pairs_1():
    assert winner("10C 10S AH 3D AC", "10D 10H AD AS JS") == 2

def test_winner_two_pairs_2():
    assert winner("10C 10S QH KD QC", "10D 10H AD AS JS") == 2



    
