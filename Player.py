# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:22:33 2018

    In this class wewill have the information of each player
    
@author: pauca
"""

class Player:
    
    def __init__(self):
        self.position = 1
        self.chips = 0
        self.card1 = 0
        self.card2 = 0
    
    
    # this funciton will change the player cards
    def changeCards(self, c1, c2) :
        self.card1 = c1
        self.card2 = c2
        
    # this function will swap the position of the player
    def swapPosition(self) :
        self.position = self.position%2 +1
        
    # this function will take the chips from player total chips
    # we asume that when we call this function the number of chips to take are less or equal to total chipsof the player
    def takeChips(self, chips) :
        self.chips -= chips
    
    