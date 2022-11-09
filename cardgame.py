""" Class definitions for implementing card games.

    Test functions use the command line for interaction.
"""


import random

class Card:
    """A standard playing card. """

    def __init__(self, rank, suit):
        """ Initialise the card.

            rank should be an integer in {1,2,...,13}
            suit should be an integer in {1,2,3,4}

        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '' + self.name_rank() + self.name_suit()

    def name_rank(self):
        """ Return a string representation of the rank. """
        if self.rank == 1:
            return 'A'
        elif self.rank == 11:
            return 'J'
        elif self.rank == 12:
            return 'Q'
        elif self.rank == 13:
            return 'K'
        else:
            return '' + str(self.rank)

    def name_suit(self):
        """ Return a string representation of the suit. """
        if self.suit == 1:
            return 'S'
        elif self.suit == 2:
            return 'H'
        elif self.suit == 3:
            return 'D'
        else:
            return 'C'

    def is_equal(self, card):
        """ Determine whether this instance is the same card as another. """
        if self.rank == card.rank and self.suit == card.suit:
            return True
        return False

    def is_higher(self, other):
        """ Determine whether this card is higher than another. """
        if self.rank > other.rank:
            return True
        return False
        
    def is_lower(self, other):
        """ Determine whether this card is lower than another. """
        if self.rank < other.rank:
            return True
        return False
        
    def test():
        """ Test the Card class.

             Run this each time the implementation of Card changes, to make
             sure the changes are correct and that no unintended effects
             are generated.

        """
        
        c1 = Card(3,3)
        c2 = Card(13,1)
        c3 = Card(8,2)
        c4 = Card(8,2)

        print('c1 (should be 3D) = ', c1)
        print('c2 (should be KS) = ', c2)
        print('c3 (should be 8H) = ', c3)

        errors = 0;

        if c1.rank != 3:
            print('ERROR: c1.rank gave ', c1.rank,
                ' but should be 3')
            errors = errors + 1
        if c2.rank != 13:
            print('ERROR: c2.rank gave ', c2.rank,
                ' but should be 13')
            errors = errors + 1
        if c3.suit != 2:
            print('ERROR: c3.suit gave ', c3.suit,
                ' but should be 2')
            errors = errors + 1
        if not c3.is_equal(c4):
            print('ERROR: c3.is_equal(c4) gave ', c3.is_equal(c4),
                ' but should be True')
            errors = errors + 1
        if c3.is_equal(c2):
            print('ERROR: c3.is_equal(c2) gave ', c3.is_equal(c4),
                ' but should be False')
            errors = errors + 1
        print('Tests complete, with ', errors, ' errors')

class Hand:
    """ A generic (unordered) hand of playing cards. """
    
    def __init__(self):
        self.cardlist = []

    def __str__(self):
        outstr = ''
        for card in self.cardlist:
            outstr = outstr + str(card) + '-'
        return outstr

    def length(self):
        """ Report how many cards are in the hand. """
        return len(self.cardlist)

    def add_card(self, card):
        """ Add the card to the hand. """
        self.cardlist.append(card)

    def play_card(self, card):
        """ Play specified card from hand.

            If card is in hand, remove it and return True.
            Otherwise return False
        """
        found = False
        i = 0
        while i < len(self.cardlist) and not found:
            if self.cardlist[i].is_equal(card):
                found = True
                self.cardlist.pop(i)
            else:
                i = i+1
        return found

    def get_highest(self):
        """ Report the highest ranked card in the hand.  """
        if len(self.cardlist) == 0:
            return None
        highcard = self.cardlist[0]
        for card in self.cardlist:
            if card.rank > highcard.rank:
                highcard = card
        return highcard
        

    def test():
        """ Test the Hand class.

             Run this each time the implementation of Hand changes, to make
             sure the changes are correct and that no unintended effects
             were generated.

        """
        
        h = Hand()
        h.add_card(Card(8,1))
        h.add_card(Card(13,4))
        h.add_card(Card(3,3))

        print('Hand h should be 8S-KC-3D-, is ', h)
        print('Highest card should be KC, is ', h.get_highest())
        print('Trying to play KC from h: ', h.play_card(Card(13,4)))
        print('Hand h should be 8S-3D-, is ', h)
        print('Highest card should be 8S, is ', h.get_highest())
        print('Trying to play 7S from h: ', h.play_card(Card(7,1)))
        print('Hand h should be 8S-3D-, is ', h)
        print('Highest card should be 8S, is ', h.get_highest())

class Board:
    """ A 'board' of cards for 'Play your cards right'. """
 
    def __init__(self):
        self.hidden = []  # the sequence of face-down cards
        self.current = None # the current face-up card
        self.revealed = [] # the sequence of previously revealed cards

    def add_card(self, card):
        """ Add the card to the hidden list. """
        self.hidden.append(card)

    def reveal_next(self):
        if len(self.hidden) == 0:
            return False 
        if self.current is not None:
            self.revealed.append(self.current)
        self.current = self.hidden.pop()
        return True

    def cards_remaining(self):
        return len(self.hidden)
        
    def current_card(self):
        return self.current

    def show_revealed(self):
        output = "["
        for card in self.revealed:
            output += str(card)
        output += "]"
        return output

class Deck:
    """ A deck of standard playing cards. """
    
    def __init__(self):
        self.cardlist = []
        for i in range(4):
            for j in range(13):
                self.cardlist.append(Card(j+1,i+1))

    def __str__(self):
        outstr = ''
        for card in self.cardlist:
            outstr = outstr + card.__str__() + '-'
        return outstr

    def length(self):
        """ Report the number of cards left in the deck. """
        return len(self.cardlist)

    def show_top_card(self):
        """ Report the top card in the deck, without removing it. """
        return self.cardlist[len(self.cardlist)-1]

    def deal_top_card(self):
        """ Remove and return the top card in the deck. """
        return self.cardlist.pop()

    def shuffle(self):
        """ Shuffle the deck. """
        random.shuffle(self.cardlist)

    def test():
        """ Test the Deck class.

             Run this each time the implementation of Deck changes, to make
             sure the changes are correct and that no unintended effects
             are generated.

        """
        
        deck = Deck()
        print('num cards in deck: ', deck.length())
        print('deck: ', deck)
        print('deck top card: ', deck.show_top_card())
        print('removing top card: ', deck.deal_top_card())
        print('deck new top card: ', deck.show_top_card())
        deck.shuffle()
        print('deck after shuffling: ', deck)
        print('num cards in deck: ', deck.length())
        for i in range(40):
            deck.deal_top_card()
        print('dealt 40 cards')
        print('num cards in deck (should be 11): ', deck.length())
        print('deck: ', deck)
        print('removing top card: ', deck.deal_top_card())
        print('deck: ', deck)
        
        
def play_game2():
    """ Play a simple betting game.

        Player is dealt a board of n cards, face down, from a shuffled deck.
        The first card in the hand is revealed.
        Player must predict whether the next card is higher or lower.
        If the player gets it wrong, player loses.
        If the player reaches the end of the hand without losing, player wins.
    """
    deck = Deck()
    deck.shuffle()
    board= Board()
    for i in range(5):
        board.add_card(deck.deal_top_card())
    board.reveal_next()
    lost = False
    while not lost and board.cards_remaining() > 0:
        previous= board.current_card()
        print('You have', board.cards_remaining(), 
              'cards left; current card is', previous); 
        ans = input('Is next card higher or lower? (h/l) ')
        ans.strip()     #remove whitespace in case user mistyped
        if ans.startswith('h') or ans.startswith('H'):
            board.reveal_next()
            print('The next card is', board.current_card())
            if board.current_card().is_higher(previous):
                print('Yay!')
            else:
                print('No! You predicted next card was higher. You lose!')
                lost = True
        elif ans.startswith('l') or ans.startswith('l'):
            board.reveal_next()
            print('The next card is', board.current_card())
            if board.current_card().is_lower(previous):
                print('Yay!')
            else:
                print('No! You predicted next card was lower. You lose!')
                lost = True
    if lost:
        print('Sorry - game over.')
    else:
        print('No more cards left. Congratulations! You win.')


def play_game1():
    """ Play a simple high-card guessing game.

        Player and system are dealt 5 cards each from a shuffled deck.
        Player must predict whether or not player has the highest ranked
        card. Both hands are then revealed, and the prediction assessed.
    """
    deck = Deck()
    deck.shuffle()
    h0 = Hand()
    h1 = Hand()
    for i in range(5):
        h0.add_card(deck.deal_top_card())
        h1.add_card(deck.deal_top_card())
    print('Your hand is: ', h0)
    ans = input('Do you have the highest card? (y/n): ')
    ans.strip()     #remove whitespace in case user mistyped
    if ans.startswith('y') or ans.startswith('Y'):
        highest = 'you'     #using strings to make output easier
    else:
        highest = 'the system'

    high0 = h0.get_highest()
    high1 = h1.get_highest()
    if high0.rank < high1.rank and highest == 'you':
        correct = False
    elif high1.rank < high0.rank and highest == 'the system':
        correct = False
    else:
        correct = True

    print('You predicted ', highest, ' had the highest card.')
    print('Your hand was: ', h0, ' with highest card ', high0)
    print('The systems hand was: ', h1, ' with highest card ', high1)
    print('Your prediction was ', correct)

def lecture_test():
    """ Test the Card class, from lecture. """
    
    c1 = Card(3,4)
    c2 = Card(8,2)
    c3 = Card(8,2)

    print(c1.rank)
    #print(c1.get_rank())
    print(c2.suit)
    #print(c2.get_suit())
    print(c3)

    if c2.is_equal(c3):
        print('Yes, c2 and c3 represent the same card (but they are different objects)')
    else:
        print('No, c2 and c3 are not the same card (and they are different objects)')
    

print("Lecture test")
lecture_test()
print()
print("Simple high card game (Aces are low ...)")
play_game1()
print()
print("Play your cards right (Aces are low ...)")
play_game2()
       
        
