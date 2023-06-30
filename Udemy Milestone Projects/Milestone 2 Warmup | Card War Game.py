'''
Warmup excercise for Milestone 2 project
Constructing a simple card game - War Game
https://en.wikipedia.org/wiki/War_(card_game)
'''
import random

# Defining global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    #understand suit
    #understand rank
    #Assign int values for card comparison
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
    
#creating test instance of the Card class:  Testing purposes
 
#two_of_hearts = Card("Hearts","Two") 
#print(two_of_hearts)
#print(two_of_hearts.suit)
#print(two_of_hearts.rank)
#print(values[two_of_hearts.rank])
#print(two_of_hearts.value)
#
#three_clubs = Card("Clubs","Three")
#print(three_clubs.rank)
#print(three_clubs.suit)
#print(three_clubs.value)

#
#print(three_clubs.value > two_of_hearts.value)



class Deck:
    # create the deck, based on the Card class above - creating a list that stores each card object
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    # Randomly shuffle the deck - method
    def shuffle(self):
        random.shuffle(self.all_cards)

    #Method to deal 1 card - grabbing 1 card from list of all_cards
    def deal_one(self):
        return self.all_cards.pop()


# Check the above works as expected:
# new_deck = Deck()
# new_deck.shuffle()
# first_card = new_deck.all_cards[0]
# bottom_card = new_deck.all_cards[-1]
# print(first_card)
# print(bottom_card)
# for card_object in new_deck.all_cards:
    # print(card_object)

# Check that deal_one method is working:
# new_deck = Deck()
# new_deck.shuffle()
# mycard = new_deck.deal_one()
# print(mycard)
# print(len(new_deck.all_cards))

class Player:

    # Hold a players current list of cards
    # Able to add or remove cards from their hand (list of card objects)
    # Able to add a single or nultiple cards to their hand/list of cards

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0) # remove from top of list

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            #list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            #for a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"player {self.name} has {len(self.all_cards)} cards"
    
        
    
# Testing the class

# new_player = Player("Mike")
# new_player.add_cards(mycard)
# print(new_player)
# print(new_player.all_cards[0])
# new_player.add_cards([mycard,mycard,mycard])
# print(new_player)
# new_player.remove_one()        
# print(new_player)


# Game setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
# print(len(player_one.all_cards))
# print((player_one.all_cards[0]))
# print(len(player_two.all_cards))
# print((player_two.all_cards[0]))

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print("-----------------")
    print(f"Round {round_num}")
    print("-----------------")
    

    if len(player_one.all_cards) == 0:
        print("Player one out of cards. Player two wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player two out of cards. Player one wins!")
        game_on = False
        break

    # Start a new round
    # Active cards in play, on table
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    print(f"Player one card matchup: {player_one_cards[-1].value}")
    print(f"Count player one hand: {len(player_one.all_cards)}")
    print(f"Player two card matchup: {player_two_cards[-1].value}")
    print(f"Count player two hand: {len(player_two.all_cards)}")

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False

        else:
            print("WAR!")
            print("-----------------")

            if len(player_one.all_cards) < 5:
                print("Player one unable to declare war")
                print("Player two wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player two unable to declare war")
                print("Player one wins!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                   
