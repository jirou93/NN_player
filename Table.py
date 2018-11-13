# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:30:39 2018

    In this class we will have a table that will contain two players and a deck.        
    Also this class will execute the hands

@author: pauca
"""

from Player import Player
from Deck import Deck

class Table:
    
    def __init__(self):
        self.player1 = Player()
        self.player1.swapPosition()
        self.player2 = Player()
        self.deck = Deck()
        self.bigBlind = 0
        self.dealer = 1
        self.pot = 0
        self.hand_number = 0
        self.hand_increase_blinds = 0
    
    # This function will take the blinds from the players
    def takeBlinds(self) :
        if dealer == 1:
            
    
    # Set the number of hands that we need to play to increase the blinds
    def setHandsToIncreaseBB(self, hands) :
        self.hand_increase_blinds = hands
    
    # Set the initial cost of the BigBlind
    def setBigBlind(self, bb) :
        self.bigBlind = bb
        
    # Set the players total chips
    def setChips(self, chips) :
        self.player1.chips = chips
        self.player2.chips = chips
        
    # Change dealer position
    def changeDealer(self) :
        self.dealer = self.dealer%2 + 1
    
    # This function will deal the cards to the two players    
    def dealCards(self) :
        c1 = self.deck.selectRandomCard()
        c2 = self.deck.selectRandomCard()
        c3 = self.deck.selectRandomCard()
        c4 = self.deck.selectRandomCard()
        if self.dealer == 1 :
            self.player1.changeCards(c1,c3)
            self.player2.changeCards(c2,c4)
        else :
            self.player1.changeCards(c2,c4)
            self.player2.changeCards(c1,c3)
    
    # This function will restart the Deck to have all the cards
    def restartDeck(self) :
        self.deck.used_cards = []
        
    
