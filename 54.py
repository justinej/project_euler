#### URgh this was a pain to code



# Poker hands
# Compare p1 and p2's hands
# Example: 7D 5D TS 9H 4H 4C 9C 2H 8C QC

### Simple count-based hands ###

def four(hand):
    nums_dict = card_dict(hand)
    for key in nums_dict:
        if nums_dict[key] == 4:
            return key
    return False

def triplet(hand):
    nums_dict = card_dict(hand)
    triplet = False
    for key in nums_dict:
        if nums_dict[key] == 3:
            return key
    return False

def pair(hand):
    nums_dict = card_dict(hand)
    pair = False
    for key in nums_dict:
        if nums_dict[key] == 2:
            return key
    return False

def two_pairs(hand):
    nums_dict = card_dict(hand)
    pair1 = None
    for key in sorted(nums_dict.keys()):
        if nums_dict[key] == 2:
            if not pair1: pair1 = key
            else: return [key, pair1]
    return False

### More complicated hands ###

def flush(hand):
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return False
    return True

def straight(hand):
    for i in xrange(1, 5):
        if hand[i][0] != hand[i-1][0] - 1:
            return False
    return True

def full_house(hand):
    has_pair = pair(hand)
    has_triplet = triplet(hand)
    if has_pair and has_triplet:
        return [has_triplet, has_pair]
    else: return False


### Helper methods ###

def card_dict(hand):
    nums_dict = dict([(x, 0) for x in xrange(2, 15)])
    for card in hand:
        nums_dict[card[0]] = nums_dict[card[0]] + 1
    return nums_dict
        
def card_nums(hand):
    # Probably should return list because tehre exist As, Qs, etc.
    priority = []
    for card in hand:
        priority.append(card[0])
    return priority

def compare_list(hand1, hand2):
    # Compare in order of list
    for i in xrange(len(hand1)):
        if hand1[i] > hand2[i]:
            return 1
        elif hand1[i] < hand2[i]:
            return 0
    # should never reach here
    raise ValueError
    return 0

### Main method### 


def best_hand(hand):
    # format in desc order of #s: [ (11, 'D'), (9, 'H') ...]
    # A is 14
    # 
    # Hand order:
    # 9 - Straight flush
    # 8 - Four of a kind
    # 7 - Full house
    # 6 - Flush
    # 5 - Straight
    # 4 - Three of a kind
    # 3 - Two pairs
    # 2 - One pair
    # 1 - High card
    #
    # Returns: (hand_code see above, priority)
    # Priority is a list of numbers or a single number
    # If list, we compare in order
    
    if straight(hand) and flush(hand):
        best = (9, card_nums(hand))
    elif four(hand):
        best = (8, four(hand))
    elif full_house(hand):
        best = (7, full_house(hand))
    elif flush(hand):
        best = (6, card_nums(hand))
    elif straight(hand):
        best = (5, card_nums(hand))
    elif triplet(hand):
        best = (4, triplet(hand))
    elif two_pairs(hand):
        best = (3, two_pairs(hand))
    elif pair(hand):
        best = (2, [pair(hand)] + card_nums(hand))
    else: best = (1, card_nums(hand))
    return best

def winner(all_cards):
    all_cards = [(x[0], x[1]) for x in all_cards.split(" ")]
    num_conversion = [(str(x), x) for x in xrange(10)]
    num_conversion += [ ('T', 10), ('J', 11), ('Q', 12), ('K', 13), ('A', 14) ]
    num_conversion = dict(num_conversion)
    all_cards = [ (num_conversion[x[0]], x[1]) for x in all_cards]

    p1_hand = best_hand(sorted(all_cards[:5], reverse=True))
    p2_hand = best_hand(sorted(all_cards[5:], reverse=True))
    if p1_hand[0] > p2_hand[0]:
        return 1
    elif p1_hand[0] < p2_hand[0]:
        return 0
    else:
        if type(p1_hand[1]) == list:
            return compare_list(p1_hand[1], p2_hand[1])
        if type(p1_hand[1]) == int:
            if p1_hand[1] > p2_hand[1]:
                return 1
            else: return 0

def run():
    filename = "poker.txt"
    f = open(filename, "r")
    ans = 0
    for line in f:
        ans += winner(line[:-1])
    f.close()
    return ans



print run()
    





