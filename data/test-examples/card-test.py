import unittest

from cards import Hand, Card

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
        
