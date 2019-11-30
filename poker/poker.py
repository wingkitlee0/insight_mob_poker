class Hand:
    def __init__(self, str_hand):
        """
        Example:
        str_hand = "2C 2H 4S AD JH"
        card_list = ["AD", "JH", "4S", "2C", "2H"]
        """
        self.str_hand = str_hand
        self.card_list = []
        for card in str_hand.split(" "):
            self.card_list.append(Card(card))
    
        self.card_list.sort(key=lambda x: x.rank, reverse=True)
        self.highest_card = self.card_list[0]
        # rank_list contains a list of ranks sorted in descending order
        self.rank_list = [card.rank for card in self.card_list]
        # sort rank_list by the number of counts of each element in descending order
        self.rank_list = sorted(self.rank_list, key = self.rank_list.count, reverse=True)

        self.same_suit = len(set([card.suit for card in self.card_list])) == 1
        # hand_type: integer from 0 to 9, indicating the type of the hand
        self.hand_type = 0 # default, with highest card
        self.set_hand_type()
        # score list is a list for comparing two hands, with hand type being the first element
        self.score_list = [self.hand_type] + self.rank_list.copy()

    def set_hand_type(self):
        """
        
        """
        if len(set(self.rank_list)) == 4: 
            self.hand_type = 1
        elif len(set(self.rank_list)) == 3:
            #two pairs or three of a kind
            if max(self.rank_list.count(num) for num in self.rank_list) == 3:
                self.hand_type = 3
            else:
                # max(..) == 2
                self.hand_type = 2
        elif len(set(self.rank_list)) == 2:
            #full house or four of a kind
            if max(self.rank_list.count(num) for num in self.rank_list) == 4:
                self.hand_type = 7
            else:
                # max(..) == 3
                self.hand_type = 6
        else:
            if self.same_suit:
                # straight flush and royal flush
                if (self.rank_list[0] - self.rank_list[-1]) == 4:
                    if self.rank_list[-1] == 10:
                        # royal flush
                        self.hand_type = 9
                    else:
                        # straight flush
                        self.hand_type = 8
                else:
                    # flush
                    self.hand_type = 5
            else:
                if (self.rank_list[0] - self.rank_list[-1]) == 4:
                    # straight
                    self.hand_type = 4
                else:
                    # highest card
                    self.hand_type = 0

class Card:
    def __init__(self, str_card):
        self.str_card = str_card # e.g. 2H
        
        self.card_dict = {'A':14, 'K':13 , 'Q':12, 'J':11}
        for i in range(2,11,1):
            self.card_dict[str(i)] = i

        if len(self.str_card) < 2:
            self.rank = None
            self.suit = None
        else:
            self.rank = self.get_rank_from_card()
            self.suit = self.str_card[-1]

    def get_rank_from_card(self):
        # "2H" -> 2
        return self.card_dict[self.str_card[:-1]]

def winner(hand1, hand2):
    """
    Args: hand1, hand2 (each Hand class)
    Return: 1 hand1 wins, 0 draw, 2 hand2 wins
    """
    
    hand1 = Hand(hand1)
    hand2 = Hand(hand2)

    if hand1.score_list > hand2.score_list:
        return 1
    elif hand1.score_list < hand2.score_list:
        return 2
    else:
        return 0
