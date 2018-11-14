# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:17:12 2018

    This class will manage all the table and select wich of the strategies NN
    the player must select in each moment
    
@author: pauca
"""

from Table import Table

class Game:
    
    
    def __init__(self) :
        self.bigBlind = 10
        self.starting_chips = 1500
        self.handsUpgradeTheBlinds = 10
        self.table = Table()
        self.table.bigBlind = self.bigBlind
        self.table.setChips(self.starting_chips)
        
    # This function will determine if the game had ended and return the winner    
    def gameEnd(self) :
        if self.table.player1.chips == 0
    
    