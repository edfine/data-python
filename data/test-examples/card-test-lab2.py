import unittest
import random

from cards import Hand, Card, Deck

class TestDeck(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()
        
    def test52(self):
        self.assertEqual(len(self.deck), 52)
        
    def test_no_dupes(self):
        seen = set()
        for card in self.deck:
            self.assertNotIn(card, seen)
            seen.add(card)
            
    def test_repr_string(self):
        "smoke test"
        self.assertIsInstance(repr(self.deck), str)
        
    def test_shuffle(self):
        deck2 = Deck()
        random.shuffle(deck2)
        self.assertNotEqual(self.deck.cards, deck2.cards)
        
    def test_deal_5(self):
        hand = self.deck.deal(5)
        self.assertEqual(len(hand), 5)
        
    def test_draw(self):
        hand = self.deck.deal(5)
        self.deck.draw(hand)
        self.assertEqual(len(hand), 6)
            
class TestCards(unittest.TestCase):
    
    def test_repr_string(self):
        self.assertIsInstance(repr(Card(rank='A', suit='clubs')), str)
            
    def test_same_card(self):
        c0 = Card(rank='A', suit='clubs')
        c1 = Card(rank='A', suit='clubs')
        self.assertEqual(c0, c1)
        
    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank='B', suit='clubs')
            
    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank='A', suit='clubsoda')
            

class TestHand(unittest.TestCase):
    
    def test_simple(self):
        hand = Hand([Card(rank='5', suit='spades')])
        self.assertEqual(hand.score(), 5)
        
    def test_soft_17(self):
        hand = Hand([
            Card(rank='A', suit='spades'),
            Card(rank='6', suit='spades'),
        ])
        self.assertEqual(hand.score(), 17)
            
    def test_hard_17(self):
        hand = Hand([
            Card(rank='A', suit='spades'),
            Card(rank='K', suit='spades'),
            Card(rank='6', suit='spades'),
        ])
        self.assertEqual(hand.score(), 17)
        
    def test_really_hard_14(self):
        hand = Hand([
            Card(rank='A', suit='spades'),
            Card(rank='A', suit='clubs'),
            Card(rank='A', suit='hearts'),
            Card(rank='A', suit='diamonds'),
            Card(rank='K', suit='spades')
        ])
        self.assertEqual(hand.score(), 14)
        
