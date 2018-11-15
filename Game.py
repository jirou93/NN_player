# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:17:12 2018

    This class will manage all the table and select wich of the strategies NN
    the player must select in each moment
    
@author: pauca
"""

from Table import Table
from PreflopController import PreflopController

class Game:
    
    # strat1 --> Strategy for Player1
    # strat2 --> Strategy for Player 2
    # strat must be a dictionary with the key string and value another dictionary
    #        with key int that determines the action (OR, 3Bet ...)
    #        and value array with the weights needed
    def __init__(self, strat1, strat2) :
        self.bigBlind = 10
        self.starting_chips = 1500
        self.handsUpgradeTheBlinds = 10
        self.table = Table()
        self.table.bigBlind = self.bigBlind
        self.table.setChips(self.starting_chips)
        self.preflop = PreflopController(strat1["PF"], strat2["PF"])
        
        
    # This function will simulate one game and return who is the winner
    def simulateGame(self) :
        while self.gameEnd() == 0 : 
            self.table.newHand()
            
        
            
    # this function will determine if the program needs to update the blinds,
    # if it needed auto increase the blinds
    def increaseBlinds(self) :
        if self.table.hand_number % self.handsUpgradeTheBlinds == 0:
            self.table.bigBlind *=2
        
    
    # This function will determine if the game had ended and return the winner   (1 or 2)
    # or will retunr 0 if the game had not end yet
    def gameEnd(self) :
        if self.table.player1.chips == 0 :
            return 2
        if self.table.player2.chips == 0 :
            return 1
        return 0
    
    
            
    
    