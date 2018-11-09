# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:04:23 2018

    In this class I will drop all the information about the deck.
    I have the full deck of cards as an array, and an array of used cards.

@author: pauca
"""

import numpy as np
import Cards

class Deck:
    
    def __init__(self) :
        # An array of ids of cards cointaining all the deck
        self.cards =  np.arange(52)
        # Array that contains all the cards that had been used before
        self.used_cards = []
        
        