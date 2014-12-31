'''
Created on Nov 9, 2014
@author: c

This class represents one state of the Turing machine.
The state has a name and 2 booleans indicating whether it is an accept/reject 
state.
'''
class State:
    def __init__(self, name, acceptState = False, startState = False):
        self.__name = name
        self.__acceptState = acceptState
        self.__startState = startState
        
        
    def setAcceptState(self, acceptState = True):
        self.__acceptState = acceptState
        

        
    def setStartState(self, startState = True):
        self.__startState = startState
        
    def isAcceptState(self):
        return self.__acceptState
    
    
    def isStartState(self):
        return self.__startState
    
    def getName(self):
        return self.__name
    