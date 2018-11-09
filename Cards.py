# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 16:43:16 2018

    This is a class that represents a Card of the hole game.
    Every card will have an ID that refers to an unic club of card and number.
    
@author: pauca
"""



class Card:
        
    # Inicialitzation of the card class with an unique ID(i)
    def __init__(self, i):
        self.id = i
        self.club = self.set_club(i)
        self.value = i%13
        if self.value == 0 :
            self.value = 13
        
        
    #This function will set every id of card to her corresponding club. 1 <= i <= 52   
    def set_club(self, i):
        # Hearts club
        if i < 14 :
            return "H"
        # Diamond club
        if i < 27 :
            return "D"
        # Spades club
        if i < 40 :
            return "S"
        # Clover club
        return "C"
        
        