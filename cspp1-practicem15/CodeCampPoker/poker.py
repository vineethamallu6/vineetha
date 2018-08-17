'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def is_straight(ranks):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    return len(set(ranks)) == 5 and (max(ranks) - min(ranks) == 4)


def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    temp = hand[0]
    i = 0
    for i in hand:
        if temp[1] != i[1]:
            return False
    return True
    

def card_rank(hand):
    ranks = sorted(['--23456789TJQKA'.index(c) for c, s in hand],reverse=True)
    return ranks
def kind(ranks, n_1):
    for r_1 in ranks:
        if ranks.count(r_1) == n_1:
            return r_1
    return 0
def two_pair(ranks):
    one = kind(ranks, 2)
    two = kind(sorted(ranks), 2)
    if one and two:
        return (one, two)
    return 0
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    
    ranks = card_rank(hand)
    if is_straight(ranks) and is_flush(hand):
        return (8, ranks)
    if kind(ranks,4):
        return (7, kind(ranks, 4), ranks)
    if kind(ranks, 3) and kind(ranks, 2):
        return (6, (kind(ranks, 3), kind(ranks, 2)))
    if is_flush(hand):
        return (5, ranks)
    if is_straight(ranks):
        return (4, ranks)
    if kind(ranks, 3):
        return (3, kind(ranks, 3), ranks) 
    if two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    if kind(ranks, 2):
        return (1, kind(ranks, 2), ranks)
    return (0, ranks)



def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''


    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
