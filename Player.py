# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:22:33 2018

    In this class wewill have the information of each player
    
@author: pauca
"""

class player:
    
    def __init__(self):
        self.position = 1
        self.blinds = 0
        self.card1 = "X"
        self.card2 = "X"
    
    
    # this funciton will change the player cards
    def changeCards(self, c1, c2) :
        self.card1 = c1
        self.card2 = c2

    # this function will change the values of the player blinds
    def changeBlinds(self, blinds) :
        self.blinds = blinds
        
    # this function will swap the position of the player
    def swapPosition(self) :
        self.position = self.position%2 +1
    
