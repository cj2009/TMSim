'''
Created on Nov 9, 2014
@author: c

This class represents a rule of the Turing machine. A rule has 2 states,
a readSymbol, a writeSymbol and a moveDirection.

The inputs are not validated by this class. The TM will validate whether the
rules are created for valid states, use valid alphabets, etc.

moveDirection must be -1 (left), 0 (stay) or 1 (right).
'''

class Rule:
    def __init__(self, state1, state2, readSymbol, writeSymbol, moveDirection):
        self.__state1 = state1
        self.__state2 = state2
        self.__readSymbol = readSymbol
        self.__writeSymbol = writeSymbol
        self.__moveDirection = moveDirection
        
        if not (moveDirection is -1 or 0 or 1):
            raise Exception("Invalid move direction!")
        
    def getState1(self):
        return self.__state1
    
    def getState2(self):
        return self.__state2
    
    def getReadSymbol(self):
        return self.__readSymbol
    
    def getWriteSymbol(self):
        return self.__writeSymbol
    
    def getMoveDirection(self):
        return self.__moveDirection