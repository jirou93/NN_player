# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:04:23 2018

    In this class I will drop all the information about the deck.
    I have the full deck of cards as an array, and an array of used cards.

@author: pauca
"""

import numpy as np
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