# file: Python_Blackjack.py

import random
import math
deck = ["Ace", "Ace", "Ace", "Ace", "King", "King", "King", "King", "Queen", "Queen", "Queen", "Queen", "Jack", "Jack", "Jack", "Jack",
 "1", "1", "1", "1", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5",
  "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9",]
values = {"Ace" : 11, "King" : 10, "Queen" : 10, "Jack" : 10, "10" : 10, "9" : 9, "8" : 8, "7" : 7, "6" : 6, "5" : 5,
 "4" : 4, "3" : 3, "2" : 2, "1" : 1}
dealers_cards = []
players_cards = []
def dealer_card_1(list):
    d_card1 = random.choice(list)
    list.remove(d_card1)
    dealers_cards.append(d_card1)
    return d_card1
def player_card_1(list):
    p_card1 = random.choice(list)
    list.remove(p_card1)
    players_cards.append(p_card1)
    return p_card1

def first_deal(a):
    d1 = dealer_card_1(a)
    p1 = player_card_1(a)
    d2 = dealer_card_1(a)
    p2 = player_card_1(a)
    #print "dealer = " + d1 + ", " + d2
    #print "player = " + p1 + ", " + p2
first_deal(deck)
print "dealer's cards = " + "[" + str(dealers_cards[0]) + ", '?'" * (len(dealers_cards) - 1) + "]"
print
print "player's cards = " + str(players_cards[0:])

# dealers_cards now has 2 values
# players_cards now has 2 values
# card_values_p = []
# card_values = []
def round_one_player(list):
    # if test == "hit" or test == "h":
        p_card1 = random.choice(list)
        list.remove(p_card1)
        players_cards.append(p_card1)
        print "players cards = " + str(players_cards)

def player_1(x):
    if x == "Hit" or x == "h" or x == "hit":
        round_one_player(deck)
    else:
        return "s"


def p1(z):
    card_values_p = []
    for card in z:
        card_values_p.append(values[card])
    if sum(card_values_p) == 21:
        return "win"
    elif sum(card_values_p) <= 21 and "Ace" not in z:
            p2 = player_1(raw_input("Hit or Stand?"))
            if p2 != "s":
                return "again"
            elif p2 == "s":
                return "stand"
    elif sum(card_values_p) > 21 and "Ace" not in z:
        return "bust"
    elif sum(card_values_p) <= 31 and "Ace" in z:
            p2 = player_1(raw_input("Hit or Stand?"))
            if p2 != "s":
                return "again"
            elif p2 == "s":
                return "stand"
    elif sum(card_values_p) > 31 and "Ace" in z:
        return "bust"



def round_one_dealer_ace(x):
    card_values = []
    for card in dealers_cards:
        card_values.append(values[card])
    if sum(card_values) > 31:
        print "Dealer Bust"
        return "dbust"
        print "!!!!You Win!!!!"
    elif sum(card_values) < 27:
        hd = dealer_card_1(deck)
        card_values.append(values[hd])
        print
        print "Dealer Hit"
        print
        print "dealer's cards = " + "[" + str(dealers_cards[0]) + ", '?'" * (len(dealers_cards) - 1) + "]"
        print
        dealer_hit_or_stand(dealers_cards)
    else:
        print "Dealer Stands"
def round_one_dealer_no_ace(x):
    card_values = []
    for card in dealers_cards:
        card_values.append(values[card])
    if sum(card_values) > 21:
        print "Dealer Bust"
        return "dbust"
        print "!!!!You Win!!!!"
    elif sum(card_values) < 17:
        hd = dealer_card_1(deck)
        card_values.append(values[hd])
        print
        print "Dealer Hit"
        print
        print "dealer's cards = " + "[" + str(dealers_cards[0]) + ", '?'" * (len(dealers_cards) - 1) + "]"
        print
        dealer_hit_or_stand(dealers_cards)
    else:
        print "Dealer Stands"
def dealer_hit_or_stand(z):
    if "Ace" in z:
        round_one_dealer_ace(z)
    else:
        round_one_dealer_no_ace(z)
def one():
    x = p1(players_cards)
    if x == "win":
        print "!!!!You Win!!!!"
        return "win"
    elif x == "bust":
        print "You Lose"
        return "bust"
    elif x == "again":
        one()
    elif x == "stand":
        z = dealer_hit_or_stand(dealers_cards)
        if z != "dbust":
            return "go"


def test():
    x = one()

    if x == "go":
        card_values = []
        card_values_p = []
        for card in players_cards:
            card_values_p.append(values[card])
        for card in dealers_cards:
            card_values.append(values[card])
        if sum(card_values) > sum(card_values_p):
            print "You Lose"
        elif sum(card_values) == sum(card_values_p):
            print "You Tied"
        elif sum(card_values) < sum(card_values_p):
            print "!!!!You Win!!!!"


test()
print
print "End Cards:"
print
print "Dealers Cards" + " = " + str(dealers_cards)
print
print "Players Cards" + " = " + str(players_cards)

# one()


#win_lose()
