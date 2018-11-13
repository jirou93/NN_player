# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:04:23 2018

    In this class I will drop all the information about the deck.
    I have the full deck of cards as an array, and an array of used cards.

@author: pauca
"""

import numpy as np
import random
from Cards import Card

class Deck:
    
    def __init__(self) :
        # An array of ids of cards cointaining all the deck
        self.cards =  np.arange(52)
        # Array that contains all the cards that had been used before
        self.used_cards = []
        
    # Adds a new card to the list of used cards
    def useCard(self, i) :
        self.used_cards.append(i)
        
    # Returns the club of a Card
    def cardClub(self, i) :
        c = Card(i)
        return c.club()
    
    # Returns the value of a card
    def cardValue(self, i) :
        c = Card(i)
        return c.value
    
    # Returns one of the unused cards from the deck and adds this card to usedCards
    def selectRandomCard(self) :
        card = random.randint(1,52)
        while self.used_cards.__contains__(card) :
            card = random.randint(1,52)
        self.used_cards.append(card)
        return card