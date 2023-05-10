import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def test_check_for_ace(self):
        game = CardGame()
        ace_card = Card("Clubs", 1)
        non_ace_card = Card("Hearts",2)
        self.assertEqual(game.check_for_ace(ace_card), True)
        self.assertEqual(game.check_for_ace(non_ace_card), False)

    def test_highest_card(self):
        game = CardGame()
        card1 = Card("Spades" ,3)
        card2 = Card("Clubs", 5)
        self.assertEqual(game.highest_card(card1, card2), card2)
        self.assertEqual(game.highest_card(card2, card1), card2)
      
    def test_cards_total(self):
        game = CardGame()
        cards = [Card("Clubs", 2), Card("Spades", 5), Card("Hearts", 10)]
        self.assertEqual(game.cards_total(cards), "You have a total of 17")  