'''
Game Play:

To play a hand of Blackjack the following steps must be followed:

Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again

'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:

    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
    
# Testing:

#card1 = Card('Hearts','Ace')
#print(card1)
#print(card1.value)
#print(card1.rank)
#print(card1.suit)

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)

    # Randomly shuffle the deck - method
    def shuffle(self):
        random.shuffle(self.deck)

    #Method to deal 1 card - grabbing 1 card from list of deck
    def deal(self):
        return self.deck.pop()
    
    def __str__(self):
        deck_contents = ''
        for card in self.deck:
            deck_contents += '\n '+ card.__str__()
        return 'The deck has: ' + deck_contents

#Testing

#test_deck = Deck()
#unshuffled deck
#print(test_deck) 
#shuffled deck
#test_deck.shuffle()
#print(test_deck) 

    
#new_deck = Deck()
#new_deck.shuffle()
#first_card = new_deck.deck[0]
#bottom_card = new_deck.deck[-1]
#print(first_card)
#print(bottom_card)

#Check that deal method is working:
#new_deck = Deck()
#new_deck.shuffle()
#mycard = new_deck.deal()
#print(mycard)
#print(len(new_deck.deck))


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Testing:

#my_card1 = Card('Hearts','Ace')
#my_card2 = Card('Hearts','King')
#my_card3 = Card('Clubs','King')
#my_hand = Hand()
#my_hand.add_card(my_card1)
#my_hand.add_card(my_card2)
#my_hand.add_card(my_card3)
#print(my_hand.value)
#print(my_hand.aces)
#my_hand.adjust_for_ace()
#print(my_hand.value)
#print(my_hand.aces)

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?: '))
        except ValueError:
            print('Sorry, a bet must be an integer')
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed {chips.total}")
            else:
                break

#Testing
#my_chips = Chips()
#print(my_chips.bet)
#take_bet(my_chips)
#print(my_chips.bet)
#print(my_chips.total - my_chips.bet)

def hit(deck,hand):
   hand.add_card(deck.deal())
   hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck,hand)
        
            
        elif x[0].lower() == 's':
            print("Player stands. Dealer is now playing.")
            playing = False

        else:
            print("Sorry, please try again!")
            continue
        break

#mydeck = Deck()
#my_hand = Hand()
#hit_or_stand(mydeck,my_hand)


def show_some(player,dealer):
    print("\nDealer's hand:")
    print("<1st card hidden>")
    print(' ',dealer.cards[1])
    print("\nPlayer's hand:", *player.cards, sep ='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.") 
    
# The game logic:

# Set up the Player's chips
player_chips = Chips()  # remember the default value is 100 

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    print("\n", "Your Total chip value: ", player_chips.total,"\n " )
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    
  
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)


    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break