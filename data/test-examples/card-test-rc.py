import unittest
import random

from cards import Deck, Hand, Card

class TestDeck(unittest.TestCase):
    def test_deck_has_52(self):
        deck = Deck()
        assert len(deck) == 52
        self.assertEqual(len(deck), 52)
        
    def test_deck_no_dupes(self):
        deck = Deck()
        set_of_cards = set(deck)
        self.assertCountEqual(set_of_cards, deck)
        
    def test_same_cards_equal(self):
        deck = Deck()
        for card in deck:
            other_card = Card(rank=card.rank, suit=card.suit)
            self.assertEqual(card, other_card)
            
    def test_bad_rank(self):
        with self.assertRaises(ValueError):
            Card(rank=42, suit='clubs')

    def test_bad_suit(self):
        with self.assertRaises(ValueError):
            Card(rank='K', suit='italian')
            
    def test_repr_deck(self):
        deck = Deck()
        self.assertIsInstance(repr(deck), str)
        
    def test_shuffle_changes_order(self):
        deck = Deck()
        initial_cards = list(deck)
        random.shuffle(deck)
        shuffled_cards = list(deck)
        self.assertNotEqual(initial_cards, shuffled_cards)
        

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
        
