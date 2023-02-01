ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
suits = 'spades hearts clubs diamonds'.split()

class Card:    
    def __init__(self, rank, suit):
        if rank not in ranks:
            raise ValueError('invalid rank')  # pragma: no cover
        if suit not in suits:
            raise ValueError('invalid suit')
        self.rank, self.suit = rank, suit
        
    def __eq__(self, other):   
        return self.rank == other.rank and self.suit == other.suit
    
    def __hash__(self):
        return hash((self.rank, self.suit))
    
    def __repr__(self):
        return f'{self.rank} {self.suit}'
    
    
class CardStack:
    
    def __init__(self, cards):
        self.cards = list(cards)
        
    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, i):
        return self.cards[i]
    
    def __repr__(self):
        return ' '.join(repr(c) for c in self)
    
    
class Deck(CardStack):
    
    def __init__(self):
        super().__init__(Card(r, s) for r in ranks for s in suits)

    def __setitem__(self, i, value):
        self.cards[i] = value

    def deal(self, n):
        return Hand([self.cards.pop() for i in range(n)])
    
    def draw(self, hand):
        hand.add(self.cards.pop())
    

class Hand(CardStack):
    
    def score(self):
        aces = [c for c in self if c.rank == 'A']
        others = [c for c in self if c.rank != 'A']
        subtotal = sum(
            int(c.rank) if c.rank.isdigit() else 10
            for c in others)
        subtotal += 11 * len(aces)
        while subtotal > 21 and aces:
            aces.pop()
            subtotal -= 10
        return subtotal
    
    def add(self, card):
        self.cards.append(card)
            
    
