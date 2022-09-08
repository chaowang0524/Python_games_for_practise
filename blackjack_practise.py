import random

# set the cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 10}

playing = True

# Classes

# Create all the cards


class Card:
    # each card has two attributes: suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # present the card as a string when it is created
    def __str__(self):
        return self.rank + ' of ' + self.suit

# Create the deck of cards


class Deck:
    def __init__(self):
        self.deck = [Card(s, r) for s in suits for r in ranks]

    def shuffle(self):
        random.shuffle(self.deck)  # shuffle the deck after it is created

    def draw(self):  # draw a card from the deck
        single_card = self.deck.pop()  # remove a card from the deck and return it
        return single_card


class Hand:  # dealer and player's hands
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # keep track of aces

    # Add a card to dealer and player's hand,
    # this card is the card drew from the deck (self.deck.pop())
    # Thus, the action completes (draw a card from the deck and put into someone's hand)
    def add_card(self, card):
        self.cards.append(card)

        # use [card.rank] as key to extract THE value from the dictinary
        # calling a method from `Card` class because it is a card
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1  # track the ace

    def adjust_for_ace(self):
        # If the total points are over 21 with aces in hand:
        while self.value > 21 and self.aces:
            # count one of the aces as 1 until the point is less than 21
            self.value -= 10
            self.aces -= 1

# Functions

# Game playing


def ask_hit_or_stand(deck, hand):
    global playing

    while True:
        ask = input("Would you like to hit or stand? Please enter 'h' or 's'")
        if ask == 'h':
            print("********************************")
            hit(deck, hand)
            print("Hit player")
            show_hand(player_hand, dealer_hand)  # check the card after drawing
            if player_hand.value < 21:
                continue
        elif ask == 's':
            print("Player stands. Dealer is playing.")
            # playing = False
            break
        # print("It didn't break out")
        break  # if correctly chosed, break out the loop and continue game

# hit card, draw a card from the deck and put into someone's hand


def hit(deck, hand):
    # use `deck` rather `Deck` because the Deck is the class
    # rather the real deck we are playing
    hand.add_card(deck.draw())  # to return the single_card
    hand.adjust_for_ace()

# show player's hand after hit


def show_hand(player, dealer):
    print("Dealer's hand: ")
    print()
    print("<Card hidden>")
    # parameter `dealer` will be `dealer_hand` so it can call the method `cards`
    print(dealer.cards[1])
    print()
    print("Player's hand: ")
    # use one line code to show all the cards in hand
    print("", *player.cards, sep='\n')

# show both players' hand when game ends


def show_all(player, dealer):
    print("********************************")
    print("Game Over")
    print("Dealer's hand: ")
    print(*dealer.cards, sep='\n')
    print("Dealer's hand = ", dealer.value)
    print()
    print("Player's hands: ")
    print(*player.cards, sep='\n')
    print("Player's hand = ", player.value)
    real_time_check_value(player_hand, dealer_hand)


def real_time_check_value(player_hand, dealer_hand):
    if player_hand.value > 21:
        player_busts()
    elif player_hand.value == 21:
        player_wins()
    elif dealer_hand.value > 21:
        dealer_busts()
    elif dealer_hand.value == 21:
        dealer_wins()

# game ending


def player_busts():
    print("Player Busts!")


def player_wins():
    print("Player Wins!")


def dealer_busts():
    print("Dealer Busts!")


def dealer_wins():
    print("Dealer Wins!")


def push():
    print("It's a push! Player and dealer tie")


# Gameplay
while True:
    print("********************************")
    print("Welcome to Blackjack!")

    # Create a deck and shuffle at once

    deck = Deck()  # `deck` is the name of the deck we are going to use in the game
    deck.shuffle()

    # Deal two cards for each player
    player_hand = Hand()  # create a hand of cards for player
    # player hand <- put card in the hand <- draw the card
    player_hand.add_card(deck.draw())
    player_hand.add_card(deck.draw())

    dealer_hand = Hand()  # create a hands of cards for dealer
    dealer_hand.add_card(deck.draw())
    dealer_hand.add_card(deck.draw())

    # check the hand when game begins
    show_hand(player_hand, dealer_hand)

    # check the hand to see if there's an immediate winner
    real_time_check_value(player_hand, dealer_hand)

    while playing:
        # Ask player to hit or stand repeatedly unti player says no
        # or player bust
        ask_hit_or_stand(deck, player_hand)

        if player_hand.value > 21:
            player_busts()
            break
        elif player_hand.value == 21:
            player_wins()
            break
        elif dealer_hand.value > 21:
            dealer_busts()
            break
        elif dealer_hand.value == 21:
            dealer_wins()
            break
        # real_time_check_value(player_hand, dealer_hand)

        # If the player chooses to stand, hit dealer until busts
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                print("********************************")
                print()
                hit(deck, dealer_hand)
                print("Hit dealer")
                if dealer_hand.value == 21:
                    dealer_wins()
                    break
                elif dealer_hand.value > 21:
                    dealer_busts()
                    break
                elif dealer_hand.value == player_hand.value:
                    push()
                    break
        break

    show_all(player_hand, dealer_hand)
    if 21 > dealer_hand.value > player_hand.value:
        dealer_wins()
    elif dealer_hand.value < player_hand.value < 21:
        player_wins()

    new_game = input("Would you like to play again? Enter 'y' or 'n'")
    if new_game == 'y':
        playing = True
    else:
        print("Thanks for playing!")
        break
